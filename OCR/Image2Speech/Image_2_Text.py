import os
import cv2
import pytesseract
from PIL import Image

def i2t(image_path):
	#1. Reading the image in grayscale
	img=cv2.imread(image_path,0)

	#2. Gaussian Blurring to remove noise and smoothen the image
	blur = cv2.GaussianBlur(img,(5,5),0)

	#3a. Adaptive Thresholding (need to tweak constants (last two) if doesn't work well)
	adapt_th = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,99,20)

	#3b. Otsu Binary Thresholding
	retval_otsu,otsu_th = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

	#Saving the image and feeding it to pytesseract
	cv2.imwrite("final.jpg",adapt_th)
	text = pytesseract.image_to_string(Image.open("final.jpg"))
	os.remove("final.jpg")
	return text

'''

#Image location will be given by --image or -i flag
ap=argparse.ArgumentParser()
ap.add_argument("--image", "-i", required=True, help="Image Location")
arguments=vars(ap.parse_args())

'''
