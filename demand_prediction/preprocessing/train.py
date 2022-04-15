import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

from demand_prediction.models.lstm.lstm import fit_model, lstm, predict_output
from demand_prediction.utils.train_test_split import get_train_test


def train(processed_df, rms_mean, output_file_path):
    return_final_df = pd.DataFrame(columns=['time_bin', 'output_frequency', 'h3_point'])
    for i in processed_df['h3_point'].unique():
        current_df = processed_df[processed_df['h3_point'] == i].drop(columns=['h3_point'], axis=1)
        train, x_train, y_train, x_test, valid, valid_df = get_train_test(current_df)
        model = lstm(x_train)
        model = fit_model(model, x_train, y_train)
        output_frequency = predict_output(model, x_test)
        scaler = MinMaxScaler(feature_range=(0, 1))
        scaler.fit(current_df.values)
        output_frequency = scaler.inverse_transform(output_frequency)
        rms = np.sqrt(np.mean(np.power((valid - output_frequency), 2)))
        rms_mean += rms
        df_temp = pd.concat([valid_df.reset_index(), pd.DataFrame(output_frequency)], axis=1)
        df_temp = df_temp.drop(columns=['frequency'], axis=1)
        df_temp['h3_point'] = i
        df_temp.columns = ['time_bin', 'output_frequency', 'h3_point']
        df_temp['output_frequency'] = df_temp['output_frequency'].apply(lambda x: int(x) if x > 0 else 0)
        return_final_df = return_final_df.append(df_temp, ignore_index=True)
    return_final_df.to_csv(output_file_path)
    return rms_mean
