import pandas as pd
import logging

from demand_prediction.preprocessing.evaluation import evaluate_model
from demand_prediction.preprocessing.fill import fill_missing_time_bins
from demand_prediction.preprocessing.frequency import get_frequency_of_rides
from demand_prediction.preprocessing.h3_binning import geo_to_h3
from demand_prediction.preprocessing.outlier_removal import remove_outliers
from demand_prediction.preprocessing.time_bin import bin_time, max_min_time_bin, stage_data
from demand_prediction.preprocessing.train import train
from demand_prediction.utils.read_inputs import read_yaml


def main():
    """
    Main function to run the demand prediction model
    """
    logging.basicConfig(level=logging.DEBUG)  # to-do: configure level from properties yaml for different environments
    try:
        # Read the inputs
        inputs = read_yaml('../properties.yaml')
        logging.info('Inputs read successfully')
        # Load the data
        demand_data = pd.read_csv(inputs['location'])
        logging.info('Data loaded successfully')
        # Remove outliers
        outlier_removed_data = remove_outliers(demand_data, float(inputs['maxlatitude']), float(inputs['maxlongitude']),
                                               float(inputs['minlatitude']), float(inputs['minlongitude']))
        logging.info('Outliers removed successfully')
        # Bin data according to h3 points
        h3_binned_data = geo_to_h3(outlier_removed_data)
        logging.info('Data binned successfully')
        # Bin data according to time
        time_binned_data = bin_time(h3_binned_data, 'created_at', int(inputs['timebinsize']))
        logging.info('Data time binned successfully')
        # Get the frequency of rides
        frequency_data = get_frequency_of_rides(time_binned_data)
        min_time_bin, max_time_bin = max_min_time_bin(demand_data, 'created_at', int(inputs['timebinsize']))
        # Fill the missing time bins with 0
        filled_data = fill_missing_time_bins(frequency_data['h3_point'].unique(), frequency_data, min_time_bin,
                                             max_time_bin)
        logging.info('Missing time bins filled successfully')
        # Staging the prepared data after processing
        processed_data = stage_data(filled_data)
        logging.info('Data staged successfully')
        # setting mean to 0
        rms_mean = int(inputs['rms'])

        # final predictions
        rms_total = train(processed_data, rms_mean, inputs['output'])
        rms_mean = evaluate_model(rms_total, processed_data['h3_point'].unique())
    except Exception as e:
        logging.error('Unexpected error has occurred while building the model', e)
    else:
        logging.info('Model built successfully')
        logging.info('RMS mean: {}'.format(rms_mean))


if __name__ == '__main__':
    main()
