# Demand Prediction
Given time-stamped locations of ride requests, this
solution effectively predicts the demand around city zones and districts

# Solution

The solution is a simple neural network that predicts the demand for each zone. The model is trained by following below steps
1. Load data
2. Outlier detection
3. H3 clustering
4. Time Binning
4. Preprocessing
5. Modeling
6. Evaluation
7. Train and test
8. Deploy

# Project layout
    .
    ├── demand_prediction        # Application Files 
    │   ├── models               # models
    │   │   ├── lstm             # contains implementation of LSTM model
    │   ├── preprocessing        # binning and outlier removals
    │   ├── eda                  # Exploratory data analysis
    │   ├── utils                # utility functions
    │   ├── demand_prediction.py # Launch point of the Application
    ├── requirements             # Requirements for the Development and Production stages 
    ├── tests                    # Unit tests
    │   ├── models               # models
    │   │   ├── lstm             # contains implementation of LSTM model
    │   ├── preprocessing        # binning and outlier removals
    ├── resources                # Resources for development stage
    ├── config                   # Resources for development stage
    │   ├── properties.yaml      # properties and configurations file
    ├── docker-compose.yml       # For launching the stages locally
    ├── dockerfile               # For creating the docker image    
    └── README.md

# Setup Instructions
To run Demand_Prediction algorithm you will need to have docker installed.
The development environment can be started by running:

`docker-compose up dev`

Or the production environment can be started by running:

`docker-compose up prod`

_The base image is provided with the data and the model. If you wish to train the model with a different set of data, same can be added in properties.py file._

output of the above command will be a csv file with the following columns:

1. Id
2. Time bin
3. forecasted requests

# How it works 
This project has two environments, development and production. The production environment does not contain the testing framework or the test code.

# Unit Testing
unit tests are available for majority of the scripts. Same can be run by running:

`docker exec <name_container> python -m unittest discover`
