
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM


def lstm(x_train):
    model = Sequential()
    model.add(LSTM(units=50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
    model.add(LSTM(units=50))
    model.add(Dense(1))
    model.compile(loss='mean_squared_error', optimizer='adam')
    return model


def fit_model(model, x_train, y_train):
    model.fit(x_train, y_train, epochs=1, batch_size=1, verbose=2)
    return model


def predict_output(model, x_test):
    return model.predict(x_test)
