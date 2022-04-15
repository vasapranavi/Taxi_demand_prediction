import pandas as pd


def bin_time(df, time_col, bin_size):
    """
    Bin the time column of a dataframe by bin_size.
    """
    df["time_bin"] = [int((pd.Timestamp(i).timestamp()) / (60 * bin_size)) for i in (df[time_col].values)]
    df = df.drop('created_at', axis=1)
    # df['time_bin'] = df['time_bin'].apply(lambda x: pd.to_datetime(x*60*bin_size, unit='s'))
    return df