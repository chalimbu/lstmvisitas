from tensorflow.keras.layers import LSTM
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dropout
import tensorflow as tf

def generar_modelo_lstm(x_data):
    model = Sequential([
                       LSTM(60,dropout=0.2,input_shape=(30,1),return_sequences=True),
                       LSTM(60,dropout=0.5,return_sequences=True),
                       LSTM(60, dropout=0.5),
                       Dense(1)])
    opt = tf.keras.optimizers.Adam()
    mse = tf.keras.losses.MeanSquaredError()
    model.compile(optimizer=opt, loss=mse)
    return model
