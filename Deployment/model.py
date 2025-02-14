# Import library yang dibutuhkan
import numpy as np
from keras.layers import Conv2D, Dense, Flatten, MaxPooling2D
from keras.models import Sequential
from keras.utils import img_to_array
from PIL import Image

# Muat model yang sudah dibuat
model = Sequential()
model.add(Conv2D(16, (3, 3), input_shape=(64, 64, 3), activation='relu'))
model.add(MaxPooling2D(2, 2))
model.add(Conv2D(32, (3, 3), activation='relu'))
model.add(MaxPooling2D(2, 2))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(2, 2))
model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(MaxPooling2D(2, 2))
model.add(Flatten())
model.add(Dense(22, activation='relu'))
model.add(Dense(6, activation='softmax'))
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.load_weights("ModelJenisSepatu.h5")


# Preparing and pre-processing the image
def preprocess_img(img_path):
    op_img = Image.open(img_path)
    img_resize = op_img.resize((64, 64))
    img2arr = img_to_array(img_resize) / 255.0
    img_reshape = img2arr.reshape(1, 64, 64, 3)
    return img_reshape


# Fungsi Prediksi
def predict_result(predict):
    pred = model.predict(predict)
    return np.argmax(pred, axis=1)
