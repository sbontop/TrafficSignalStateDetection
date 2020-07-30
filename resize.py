from os import walk
import cv2

"""
This function reads pictures located in three different directories that are: /43, /44 y /45 with root ./colores-semaforos
,resizes them to 32*32 pixels because that is required by the model to work properly and write the picture resized in the directory \
./myData/43, ./myData/44 and ./myData/45 directory respectively
Note: Every time new pictures are added to the training set should be resized in order to keep 32*32 format 
and add them to the ./myData/43, ./myData/44 and ./myData/45 directory respectively
"""
def resize_training_set():
	no_folder = 43
	no_files_read = 0
	for i in range(3):
		for (dirpath, dirnames, filenames) in walk("./colores-semaforos/" + str(no_folder) + "/"):
			for filename in filenames:
				no_files_read += 1
				original_img = cv2.imread("./colores-semaforos/" + str(no_folder) + "/" + filename, cv2.IMREAD_UNCHANGED)
				resized_img = cv2.resize(original_img, (32, 32), interpolation = cv2.INTER_AREA)
				cv2.imwrite("./myData/" + str(no_folder) + "/" + filename, resized_img)
				#print("Original Dimensions: ", original_img.shape," Resized Dimensions: ", resized_img.shape)
		print("No. Folder Read: ", no_folder, " No. Files Read: ", len(filenames))
		no_folder += 1
	print("Total Number of Files Read: ", no_files_read)

