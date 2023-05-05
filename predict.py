import np as np
from PIL import Image
from keras.models import load_model
import numpy as np
import tensorflow

model_01 = load_model('model.h5')
img = Image.open('test3.jpeg').convert('L').resize((150, 150), Image.ANTIALIAS)
img = np.array(img)

array=model_01.predict(img[None,:,:])

largest_number = 0
i=0
for number in array[0]:
    if number > largest_number:
        largest_number = i
    i=i+1



print(largest_number)
