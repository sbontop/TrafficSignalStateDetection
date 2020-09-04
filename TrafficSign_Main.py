import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
from keras.utils.np_utils import to_categorical
from keras.layers import Dropout, Flatten
from keras.layers.convolutional import Conv2D, MaxPooling2D
import cv2
from sklearn.model_selection import train_test_split
import pickle
import os
import pandas as pd
import random
from keras.preprocessing.image import ImageDataGenerator
 

rutaImagenes = "datos" # carpeta con todas las carpetas de las clases
archivoLabels = 'labels.csv' # archivo con nombres de las clases
dimensionImagenes = (50,50,3) # dimensiones de las imáges a trabajar

# Hiperparametros
tamanoBatch=18   #cantidad de datos a procesar 
epocas=85
radioTest = 0.1    # if 1000 imagenes split will 200 for testing
radioValidacion = 0.1 # if 1000 imagenes 20% of remaining 800 will be 160 for validation
 
# Importar Imágenes
conteo = 0
imagenes = []
numeroClase = []
clasesDirectorio = os.listdir(rutaImagenes)
print("Total de clases detectadas:",len(clasesDirectorio))
numeroClases=len(clasesDirectorio)
print("Importando clases.....")
for x in range (0,len(clasesDirectorio)):
    listaImagenes = os.listdir(rutaImagenes+"/"+str(conteo))
    for y in listaImagenes:
        imagenActual = cv2.imread(rutaImagenes+"/"+str(conteo)+"/"+y)
       	imagenes.append(imagenActual)
        numeroClase.append(conteo)
    print(conteo, end =" ")
    conteo +=1
print(" ")
imagenes = np.array(imagenes)
numeroClase = np.array(numeroClase)
 
# Dividir datos
XEntrenamiento, XTest, YEntrenamiento, YTest = train_test_split(imagenes, numeroClase, test_size=radioTest)
XEntrenamiento, XValidacion, YEntrenamiento, YValidacion = train_test_split(XEntrenamiento, YEntrenamiento, test_size=radioValidacion)
 
# XEntrenamiento = Arreglo de imágenes a entrenar
# YEntrenamiento = Correspondiente id de clase
 
# Chequear si número de imágenes se conecta con el número de labels para cada datos set
print("Formas de datos ")
print("Entrenamiento",end = "");print(XEntrenamiento.shape,YEntrenamiento.shape)
print("Validacion",end = "");print(XValidacion.shape,YValidacion.shape)
print("Pruebas",end = "");print(XTest.shape,YTest.shape)
assert(XEntrenamiento.shape[0]==YEntrenamiento.shape[0]), "El número de imágenes no es igual al número de labels del training set"
assert(XValidacion.shape[0]==YValidacion.shape[0]), "El número de imágenes no es igual al número de labels del set de validación"
assert(XTest.shape[0]==YTest.shape[0]), "El número de imágenes no es igual al número de labels in el set de pruebas"
assert(XEntrenamiento.shape[1:]==(dimensionImagenes)),"Las dimesiones de las images del training set son incorrectas"
assert(XValidacion.shape[1:]==(dimensionImagenes)),"Las dimesiones de las images del set de validación son incorrectas"
assert(XTest.shape[1:]==(dimensionImagenes))," Las dimensiones de las imágenes de prueba son incorrectas"
 
 
# Leer del archivo csv de clases
datos=pd.read_csv(archivoLabels)
print("Forma de datos ",datos.shape,type(datos))
datos.head(3)
 
# Mostrar ciertas imágenes de pruebas de todas las clases
numeroMuestras = []
columnas = 5
totalClases = numeroClases
fig, axs = plt.subplots(nrows=totalClases, ncols=columnas, figsize=(5, 300))
fig.tight_layout()
for i in range(columnas):
    for j,row in datos.iterrows():
        x_selected = XEntrenamiento[YEntrenamiento == j]
        axs[j][i].imshow(x_selected[random.randint(0, len(x_selected)- 1), :, :], cmap=plt.get_cmap("gray"))
        axs[j][i].axis("off")
        if i == 2:
            axs[j][i].set_title(str(j)+ "-"+row["Name"])
            numeroMuestras.append(len(x_selected))
 
 
# Mostrar un cuadro de barras mostrando numero de muestras por cada categoría
print(numeroMuestras)
plt.figure(figsize=(12, 4))
plt.bar(range(0, totalClases), numeroMuestras)
plt.title("Distribucion del dataset de entranamiento")
plt.xlabel("Numero de clases")
plt.ylabel("Numero de imágenes")
plt.show()
 
# Preprocesamiento de imágenes
 
def escalaGrises(imagen):
    imagen = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
    return imagen
def equalize(imagen):
    imagen =cv2.equalizeHist(imagen)
    return imagen
def preprocessing(imagen):
    imagen = escalaGrises(imagen)   
    imagen = equalize(imagen)      
    imagen = imagen/255        
    return imagen
 
XEntrenamiento=np.array(list(map(preprocessing,XEntrenamiento)))
XValidacion=np.array(list(map(preprocessing,XValidacion)))
XTest=np.array(list(map(preprocessing,XTest)))
 
# Agregar profundidad de 1
XEntrenamiento=XEntrenamiento.reshape(XEntrenamiento.shape[0],XEntrenamiento.shape[1],XEntrenamiento.shape[2],1)
XValidacion=XValidacion.reshape(XValidacion.shape[0],XValidacion.shape[1],XValidacion.shape[2],1)
XTest=XTest.reshape(XTest.shape[0],XTest.shape[1],XTest.shape[2],1)

# Aumento de imágenes: conseguir representación genérica
datosGenerados= ImageDataGenerator(width_shift_range=0.1,   # 0.1 = 10%     IF MORE THAN 1 E.G 10 THEN IT REFFERS TO NO. OF  PIXELS EG 10 PIXELS
                            height_shift_range=0.1,
                            zoom_range=0.2,  # 0.2 MEANS CAN GO FROM 0.8 TO 1.2
                            shear_range=0.1,  # MAGNITUDE OF SHEAR ANGLE
                            rotation_range=10)  # DEGREES
datosGenerados.fit(XEntrenamiento)
batches= datosGenerados.flow(XEntrenamiento,YEntrenamiento,batch_size=20) 
Xbatch,Ybatch = next(batches)
 
 
YEntrenamiento = to_categorical(YEntrenamiento,numeroClases)
YValidacion = to_categorical(YValidacion,numeroClases)
YTest = to_categorical(YTest,numeroClases)
 
# modeloo de red convolucional
def generarModelo():
    numeroFIltros=60
    tamanoFiltros=(5,5)
    tamanoFiltrosSegundaCapa=(3,3)
    tamanoPool=(2,2) 
    numeroNodosMLP = 500  
    modelo = Sequential()
    
    modelo.add((Conv2D(numeroFIltros//2,tamanoFiltros,input_shape=(dimensionImagenes[0],dimensionImagenes[1],1),activation='relu')))
    modelo.add((Conv2D(numeroFIltros//2, tamanoFiltros, activation='relu')))
    modelo.add(MaxPooling2D(pool_size=tamanoPool))
 
    modelo.add((Conv2D(numeroFIltros, tamanoFiltrosSegundaCapa,activation='relu')))
    modelo.add((Conv2D(numeroFIltros , tamanoFiltrosSegundaCapa, activation='relu')))
    modelo.add(MaxPooling2D(pool_size=tamanoPool))
    
    modelo.add((Conv2D(numeroFIltros, tamanoFiltrosSegundaCapa,activation='relu')))
    modelo.add((Conv2D(numeroFIltros , tamanoFiltrosSegundaCapa, activation='relu')))
    modelo.add(MaxPooling2D(pool_size=tamanoPool))
 
    modelo.add(Flatten())
    modelo.add(Dense(numeroNodosMLP,activation='relu'))
    modelo.add(Dropout(0.5))
    modelo.add(Dense(numeroClases,activation='softmax'))
    modelo.compile(Adam(lr=0.001),loss='categorical_crossentropy',metrics=['accuracy'])
    return modelo
 
 
# Entrenar
modelo = generarModelo()
print(modelo.summary())
history=modelo.fit_generator(datosGenerados.flow(XEntrenamiento,YEntrenamiento,batch_size=tamanoBatch),epochs=epocas,validation_data=(XValidacion,YValidacion),shuffle=1)
 
# Gráficos de resultados
plt.figure(1)
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.legend(['training','validacion'])
plt.title('perdida')
plt.xlabel('epoca')
plt.figure(2)
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.legend(['training','validacion'])
plt.title('Acurracy')
plt.xlabel('epoca')
plt.show()
score =modelo.evaluate(XTest,YTest,verbose=0)
print('Resultado prueba :',score[0])
print('Accuracy de test :',score[1])

# Gudardar modelo y arquitectura en un solo archivo
modelo.save("model.h5")
print("Guardar modelo a disco")
