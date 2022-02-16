import os
from keras.preprocessing import image
from keras.applications import densenet
import numpy as np
import pickle
import re
from scipy.spatial.distance import cosine

model = densenet.DenseNet201(include_top=False, weights='imagenet', input_shape=(256, 256, 3), pooling='avg', classes=1000)

print(os.listdir())
with open('../encodings.txt', 'rb') as fp:
    enc_list = pickle.load(fp)
with open('../enc_names.txt', 'rb') as fp:
    names_list = pickle.load(fp)


def get_encodings(_img):
    _img = image.img_to_array(_img)
    _img = image.smart_resize(_img, size=(256, 256))
    _img = np.expand_dims(_img, axis=0)
    _enc = densenet.preprocess_input(_img)
    _enc = model.predict(_enc)
    return _enc


def get_recipes(img):
    enc = get_encodings(img)
    similarity_list = []
    recipe_names_list = []
    for i in enc_list:
        similarity = cosine(i, enc)
        similarity_list.append(1-similarity)
    l = sorted(zip(similarity_list, names_list), reverse=True)
    for i in range(len(l)):
        name_in_list = l[i][1]
        s = re.sub(r'[0-9]+.jpg', "", name_in_list)
        if s not in recipe_names_list:
            recipe_names_list.append(s)
        if len(recipe_names_list) >= 10:
            break

    return recipe_names_list
