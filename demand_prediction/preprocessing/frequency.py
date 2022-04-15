
def get_frequency_of_rides(df):
    """
    This function calculates the frequency of rides for each hour of the day.
    The result is a dataframe with the hour and the frequency of rides.
    """
    return df.groupby(['h3_point', 'time_bin']).size().to_frame(name='frequency').reset_index()