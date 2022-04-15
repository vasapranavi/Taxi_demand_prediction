import h3


def geo_to_h3(df):
    """
    Converts a lat/lon pair to a hexagonal 3D hash.
    """
    df['h3_point'] = df.apply(lambda x: h3.geo_to_h3(lat=x['latitude'], lng=x['longitude'], resolution=5), axis=1)
    df = df.drop(['latitude', 'longitude'], axis=1)
    return df
