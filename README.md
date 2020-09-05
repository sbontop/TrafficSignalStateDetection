# Traffic Signal State Detection
Artifficial Intelligence project aims to classify traffic signs using convolutional neural network (CNN) | OpenCV Python.

## Setup
1. Install Python Development Environment in your system (in our case`Ubuntu 18.04`):
  - `sudo apt update`
  - `sudo apt install python3-dev python3-pip`
  - `sudo pip3 install -U virtualenv  # system-wide install`
  
2. Create virtual environment (recommended):
  - `virtualenv --system-site-packages -p python3 ./venv`
3. Activate Virtual Environment (just in case exists):
  - `source ./venv/bin/activate  # sh, bash, ksh, or zsh`
> Once virtual environment is active, shell window will show the prefix `(venv)`

4.  Install packages in virtual environment without affecting your system configuration. First, update `pip`: 
  - `pip3 install --upgrade pip`
  - `pip3 list  # show packages installed within the virtual environment`
5. Exit virtual environment:
  - `deactivate  # don't exit until you're done using TensorFlow or the other libraries`
6. Install all packages required via `pip`:
  - `pip3 install -r requirements.txt`
7. Training Phase:
  - `python3 TrafficSign_Main.py`
> In case compiled successfully 
> `model.h5` file should be generated
8. Testing Phase:

8.1 Early Stage Testing Phase:
- `python3 TrafficSignTest.py`
> The image selected for this test should be located in root directory and modify the name of the image read in variables `img` and `imgOrignal` in `TrafficSignTest.py` file

> Note: This script was used for early testing stage, and now we have developed a web application as a GUI where the user selects the image to test
> The web application can be found in the `./Interfaz/SemVisorIA/` directory. This folder contains the instructions to run the GUI

8.2 Web Application Visualization
> To run the GUI please visit `./Interfaz/SemVisorIA/` directory.

## Add Aditional Training Dataset
1. Select the Images for the training
2. Classify the images manually
3. Define the class name and class number in the `./label.csv` file
4. Load Images to `./colores-semaforos/${class_number}` directory, considering `${class_number}` is the number of the class in CSV file
5. Append class name and class number to the `getClassName` function in `./TrafficSignTest.py` file for early stage test phase or in `getClassName` function in `./IA/SemVisorIA/reconocimiento/IA.py` file for GUI test phase
6. Run `./resize.py` file that takes all the images located in `./colores-semaforos/` directory, and then are resized to 50x50 pixels and copied to `./datos/${class_number}` directory
