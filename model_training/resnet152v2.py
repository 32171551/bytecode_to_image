import tensorflow_addons as tfa
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from tensorflow import keras

import os
import pathlib

data_path = "C:\\Users\\fight\\Desktop\\test\\test\\data"
data_dir = pathlib.Path(data_path)

img_height =  256
img_width = 64
batch_size = 36

train_ds = tf.keras.utils.image_dataset_from_directory(
  data_dir,
  validation_split=0.2,
  seed=1234,
  subset='training',
  image_size=(img_height, img_width),
  batch_size=batch_size)

val_ds = keras.utils.image_dataset_from_directory(
  data_dir,
  validation_split=0.2,
  seed=1234,
  subset='validation',
  image_size=(img_height, img_width),
  batch_size=batch_size)

class_names = train_ds.class_names

model = tf.keras.models.load_model('./resnet1000.h5')
num_classes = len(class_names)
print(type(num_classes))
class_names = val_ds.class_names

labels = np.concatenate([y for x, y in val_ds], axis=0)
# print(labels)
y_true = tf.one_hot(labels, num_classes)
# print(y_true)

f1 = tfa.metrics.F1Score(num_classes=num_classes, average='micro')
y_pred = model.predict(val_ds)
f1.update_state(y_true, y_pred)
result = f1.result()
print(result.numpy())



df = pd.DataFrame(columns=['name', 'f1score'])
df['name'] = class_names
df['f1score'] = result.numpy()
print(df)
#
# for idx, pred in enumerate(y_pred):
#   print(np.argmax(pred), np.argmax(y_true[idx]))