import yaml
import logging


def read_yaml(filename):
    """Read from yaml file."""
    try:
        with open(filename, 'r') as f:
            documents = yaml.safe_load_all(f)
            dictionary = {}
            for document in documents:
                for key, value in document.items():
                    dictionary[key] = value
            return dictionary
    except FileNotFoundError:
        logging.error("File {} not found".format(filename))