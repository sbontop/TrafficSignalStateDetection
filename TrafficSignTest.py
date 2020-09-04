import numpy as np
import cv2
import pickle
from keras.models import load_model
 
# Cargar modelo
# Para salir del testeo presionar Ctrl+C en línea de comandos de linux

modelo = load_model('model.h5')

fuente = cv2.FONT_HERSHEY_SIMPLEX

# Imprimir detalles del modelo.
print(modelo.summary())

def grayscale(img):
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    return img
def equalize(img):
    img =cv2.equalizeHist(img)
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
  
# Leer imagen de prueba

while True:
    imgOrignal = cv2.imread('rojo5.jpeg', 1)
    imgOrignal = cv2.resize(imgOrignal, (600,338))

    # Procesar imagen
    img = cv2.imread('rojo5.jpeg', 1)
    img = cv2.resize(img, (50, 50))
    img = preprocessing(img)
    img = img.reshape(1, 50, 50, 1)
    cv2.putText(imgOrignal, "Clase: " , (20, 35), fuente, 0.75, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.putText(imgOrignal, "Probabilidad: ", (20, 75), fuente, 0.75, (0, 0, 255), 2, cv2.LINE_AA)

    # Predecir imagen
    predicciones = modelo.predict(img)
    indiceClase = modelo.predict_classes(img)
    valorProbabilidad =np.amax(predicciones)
    print("Predicciones", predicciones, "Indice de clase: ", indiceClase, "Valor de probabilidad", valorProbabilidad)
    cv2.putText(imgOrignal,str(indiceClase)+" "+str(getClassName(indiceClase)), (120, 35), fuente, 0.75, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.putText(imgOrignal, str(round(valorProbabilidad*100,2) )+"%", (180, 75), fuente, 0.75, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.imshow("Resultado", imgOrignal)

    if cv2.waitKey(1) and 0xFF == ord('q'):
        break