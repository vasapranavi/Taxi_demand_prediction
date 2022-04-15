from demand_prediction.utils.read_inputs import read_yaml


def main():
    """
    Main function to run the demand prediction model
    """
    # Read the inputs
    inputs = read_yaml('../properties.yaml')