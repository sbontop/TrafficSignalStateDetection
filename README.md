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
> Actually we have been testing with training set pictures to validate CNN learning
> and also we are in search of more pictures to add to the training set 
  - `python3 TrafficSignTest.py`
> Note: This script was used for early testing stage, and now we have developed a web application as a GUI where the user selects the image to test.
> The web application can be found in the 'Interfaz/SemVisorIA' folder in root directory. This folder contains instructions to run the GUI
