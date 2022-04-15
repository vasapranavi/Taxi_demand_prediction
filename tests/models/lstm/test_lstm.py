import unittest
import numpy as np

from demand_prediction.models.lstm import lstm


class Test(unittest.TestCase):

    def test_lstm_init(self):
        """
        Test LSTM model initialization
        """
        model = lstm.lstm(np.array([[1]]))
        assert model.input_shape == (None, 1, 1)
        assert model.output_shape == (None, 1)

    def test_fit_model(self):
        """
        Test LSTM model fitting
        """

    def test_predict_output(self):
        """
        Test LSTM model prediction
        """


if __name__ == '__main__':
    # begin the unittest.main()
    unittest.main()
