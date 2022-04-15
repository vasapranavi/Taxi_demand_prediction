"""Remove outliers from the data."""


def remove_outliers(df, lat_max, lon_max, lat_min, lon_min):
    """
    Removes the outliers from the dataframe
    """
    # Remove the outliers
    df = df[
        ((df.latitude <= lat_max) & (df.longitude <= lon_max) & (df.latitude >= lat_min) & (df.longitude >= lon_min))]
    return df
