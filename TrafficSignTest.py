import numpy as np
import cv2
import pickle
from keras.models import load_model
 
#############################################
 
frameWidth= 640         # CAMERA RESOLUTION
frameHeight = 480
brightness = 180
#threshold = 0.75         # PROBABLITY THRESHOLD
threshold = -1
font = cv2.FONT_HERSHEY_SIMPLEX
##############################################
 
# SETUP THE VIDEO CAMERA
#cap = cv2.VideoCapture(0)

#cap.set(3, frameWidth)
#cap.set(4, frameHeight)
#cap.set(10, brightness)

# IMPORT THE TRANNIED MODEL
#pickle_in=open("model_trained.p","rb")  ## rb = READ BYTE
#model=pickle.load(pickle_in)

# load model
model = load_model('model.h5')
# summarize model.
print(model.summary())

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
    if classNo == 0: return 'red'
    elif classNo == 1: return 'yellow'
    elif classNo == 2: return 'green'
 
while True:
 
    # READ IMAGE
    # success, imgOrignal = cap.read()
    imgOrignal = cv2.imread('verde10.png', 1)
 
    # PROCESS IMAGE
    # img = np.asarray(imgOrignal)
    img = cv2.imread('verde10.png', 1)
    img = cv2.resize(img, (32, 32))
    img = preprocessing(img)
    cv2.imshow("Processed Image", img)
    img = img.reshape(1, 32, 32, 1)
    cv2.putText(imgOrignal, "CLASS: " , (20, 35), font, 0.75, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.putText(imgOrignal, "PROBABILITY: ", (20, 75), font, 0.75, (0, 0, 255), 2, cv2.LINE_AA)
    # PREDICT IMAGE
    predictions = model.predict(img)
    classIndex = model.predict_classes(img)
    probabilityValue =np.amax(predictions)
    print("predictions", predictions, "classIndex: ", classIndex, "probabilityValue", probabilityValue)
    if probabilityValue > threshold:
        #print(getCalssName(classIndex))
        cv2.putText(imgOrignal,str(classIndex)+" "+str(getClassName(classIndex)), (120, 35), font, 0.75, (0, 0, 255), 2, cv2.LINE_AA)
        cv2.putText(imgOrignal, str(round(probabilityValue*100,2) )+"%", (180, 75), font, 0.75, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.imshow("Result", imgOrignal)
 
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break
