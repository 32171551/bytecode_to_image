import matplotlib.pyplot as plt
import numpy as np
import PIL
import tensorflow as tf
import pandas as pd
from tensorflow.keras.applications import resnet_v2, vgg16, vgg19
# from tensorflow import keras
from tensorflow.keras import layers
# from tensorflow.keras.models import Sequential

import os
import pathlib

data_path = "/home/aiia/daeun/data/test/"
data_dir = pathlib.Path(data_path)

img_height =  512
img_width = 128
batch_size = 16

train_ds = tf.keras.utils.image_dataset_from_directory(
  data_dir,
  validation_split=0.2,
  seed=1234,
  subset='training',
  image_size=(img_height, img_width),
  batch_size=batch_size)

val_ds = tf.keras.utils.image_dataset_from_directory(
  data_dir,
  validation_split=0.2,
  seed=1234,
  subset='validation',
  image_size=(img_height, img_width),
  batch_size=batch_size)

class_names = train_ds.class_names

num_classes = len(class_names)
train_data = train_ds.map(lambda x, y: (x, tf.one_hot(y, depth=num_classes)))
val_data = val_ds.map(lambda x, y: (x, tf.one_hot(y, depth=num_classes)))

epochs = 500

model = resnet_v2.ResNet152V2(include_top=True, weights=None, input_shape=(img_height, img_width, 3), pooling=max, classes=num_classes)

model.compile(loss=tf.keras.losses.CategoricalCrossentropy(from_logits=False), metrics=['accuracy'], optimizer='adam')

# checkpoint_filepath = './checkpoint/mymodel_{epoch}'
# model_checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(
#   filepath=checkpoint_filepath,
#   monitor='val_accuracy',
#   mode='max',
#   save_best_only=True
# )
filepath = "/home/aiia/daeun/data/test_check_point/saved-model-{epoch:02d}-{val_accuracy:.2f}.h5"
checkpoint = tf.keras.callbacks.ModelCheckpoint(filepath, monitor='val_accuracy', verbose=1, save_best_only=True, mode='max')

history = model.fit(train_data, validation_data=val_data, epochs=epochs, callbacks=[checkpoint])

# history = model.fit(train_ds, validation_data=val_ds, epochs=epochs)


model.save(filepath)

acc = history.history['accuracy']
val_acc = history.history['val_accuracy']

loss = history.history['loss']
val_loss = history.history['val_loss']

epochs_range = range(epochs)

df = pd.DataFrame.from_dict(history.history)
df.to_excel('test_history.xlsx')
