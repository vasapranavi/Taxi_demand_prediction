import pandas as pd

from demand_prediction.preprocessing.h3_binning import geo_to_h3
from demand_prediction.preprocessing.outlier_removal import remove_outliers
from demand_prediction.preprocessing.time_bin import bin_time
from demand_prediction.utils.read_inputs import read_yaml


def main():
    """
    Main function to run the demand prediction model
    """
    # Read the inputs
    inputs = read_yaml('../properties.yaml')

    # Load the data
    demand_data = pd.read_csv(inputs['location'])

    # Remove outliers
    outlier_removed_data = remove_outliers(demand_data, float(inputs['maxlatitude']), float(inputs['maxlongitude']),
                                           float(inputs['minlatitude']), float(inputs['minlongitude']))

    # Bin data according to h3 points
    h3_binned_data = geo_to_h3(outlier_removed_data)

    # Bin data according to time
    time_binned_data = bin_time(h3_binned_data, 'created_at', int(inputs['timebinsize']))