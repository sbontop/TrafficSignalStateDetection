import numpy as np
import cv2
from keras.models import load_model
from .models import Imagen
import os
import pdb

threshold = -1
font = cv2.FONT_HERSHEY_SIMPLEX

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = BASE_DIR.replace('\\','/')
# load model
dir_model = os.path.join(BASE_DIR,'reconocimiento', 'model.h5').replace('\\','/')
model = load_model(dir_model)


# summarize model.
def grayscale(img):
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    return img

def equalize(img):
    img = cv2.equalizeHist(img)
    return img

def preprocessing(img):
    img = grayscale(img)
    img = equalize(img)
    img = img/255
    return img

def getClassName(classNo):
    if classNo == 0: return 'rojo'
    elif classNo == 1: return 'amarillo'
    elif classNo == 2: return 'verde'
 
def getResults(imagen):
    res = {}
    res['imagen'] = imagen
    if imagen:
        ruta = BASE_DIR + imagen.imagen.url
        img = cv2.imread(ruta, 1)
        img = cv2.resize(img, (32, 32))
        img = preprocessing(img)
        img = img.reshape(1, 32, 32, 1)

        # PREDICT IMAGE
        predictions = model.predict(img)
        classIndex = model.predict_classes(img)
        probabilityValue = np.amax(predictions)
        
        res['tpassed'] = probabilityValue > threshold
        res['className'] = str(getClassName(classIndex))
        res['classIndex'] = str(classIndex)
        res['probabilityValue'] = str(round(probabilityValue*100,2))
    return res

    
        