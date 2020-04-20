import os
import tensorflow as tf

def callback_guardar(checkpoint_path):
    if (type(checkpoint_path) not in [str]):
        raise TypeError("la ruta debe ser un string")
    # guardar el modelo
    checkpoint_dir = os.path.dirname(checkpoint_path)
    return tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_path,
                                                     save_weights_only=True,
                                                     verbose=1)