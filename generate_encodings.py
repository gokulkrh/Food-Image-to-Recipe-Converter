# This script generates encodings for all the images in the dataset and
# saves it in a txt file and the names of the recipes in another txt file.
# Make sure to change the file paths before running the script.

import os
import numpy as np
from keras.preprocessing import image
from keras.applications import densenet
import pickle

model = densenet.DenseNet201(include_top=False, weights='imagenet', input_shape=(256, 256, 3), pooling='avg', classes=1000)


def get_encodings(_img):
    _img = image.img_to_array(_img)
    _img = np.expand_dims(_img, axis=0)
    _enc = densenet.preprocess_input(_img)
    _enc = model.predict(_enc)
    return _enc


if __name__ == '__main__':
    names_list = os.listdir("Dataset/images")
    encodings_list = []
    c = 0
    for i in names_list:
        image_path = "./Dataset/images/" + i
        img = image.load_img(image_path, target_size=(256, 256))
        encoding = get_encodings(img)
        encodings_list.append(encoding)
        c += 1
        print(c)
    print(len(names_list), len(encodings_list))
    with open('encodings.txt', 'wb') as file:
        pickle.dump(encodings_list, file)
    with open('enc_names.txt', 'wb') as file:
        pickle.dump(names_list, file)
