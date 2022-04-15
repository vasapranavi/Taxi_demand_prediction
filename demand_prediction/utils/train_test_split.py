from sklearn.preprocessing import MinMaxScaler
import numpy as np


def get_train_test(df, percentage_test=0.2):
    dataset = df.values
    train = dataset[0:(int((1-percentage_test) * len(df))), :]
    valid = dataset[(int((1-percentage_test) * len(df))):, :]
    valid_df = df.iloc[(int((1-percentage_test) * len(df))):, :]
    # converting dataset into x_train and y_train
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(dataset)
    x_train, y_train = [], []
    for i in range(60, len(train)):
        x_train.append(scaled_data[i - 60:i, 0])
        y_train.append(scaled_data[i, 0])
    x_train, y_train = np.array(x_train), np.array(y_train)
    x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
    inputs = df[len(df) - len(valid) - 60:].values
    inputs = inputs.reshape(-1, 1)
    inputs = scaler.transform(inputs)
    x_test = []
    for i in range(60, inputs.shape[0]):
        x_test.append(inputs[i - 60:i, 0])
    x_test = np.array(x_test)
    x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
    return train, x_train, y_train, x_test, valid, valid_df
