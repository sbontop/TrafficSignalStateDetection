# Traffic Signal State Detection
Artifficial Intelligence project aims to classify traffic signs using convolutional neural network (CNN) | OpenCV Python.

The libraries required to install before running the project are located in requirements.txt file. You can install all of them with the command:

## Setup
1. Instala el entorno de desarrollo Python en tu sistema (Ubuntu 18.04 en mi caso):
  `sudo apt update`
  `sudo apt install python3-dev python3-pip`
  `sudo pip3 install -U virtualenv  # system-wide install`
  
2. Crea un entorno virtual (recomendado):
`virtualenv --system-site-packages -p python3 ./venv`
3. Activa el entorno virtual (en caso de haberlo creado):
`
source ./venv/bin/activate  # sh, bash, ksh, or zsh
`
> Cuando virtualenv está activo, la solicitud del shell tiene el prefijo `(venv)`

4.  Instala paquetes dentro de un entorno virtual sin afectar la configuración del sistema host. Primero, actualiza `pip`: 
`pip3 install --upgrade pip`
`pip3 list  # show packages installed within the virtual environment`
5. Para salir del entorno virtual:
`deactivate  # don't exit until you're done using TensorFlow or the other libraries`
6. Instala todas las librerias necesarias via `pip`:
`pip3 install -r requeriments.txt`
7. Fase de entrenamiento:
`python3 TrafficSign_Main.py`
> En caso de haber compilado exitosamente el script del paso anterior 
> se debe haber generado el modelo de la red neuronal convolucional con el nombre `model.h5`
8. Fase de Prueba:
> Por ahora se probaran con imagenes del training set para comprobar que la red este aprendiendo y que tanto lo esta haciendo
> Ademas no contamos con suficientes datos para que tenga validez externa por ahora. 
`python3 TrafficSignTest.py`
