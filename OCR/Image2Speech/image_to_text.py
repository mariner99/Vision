import os
import cv2
import argparse
import pytesseract
from PIL import Image

#Image location will be given by --image or -i flag
ap=argparse.ArgumentParser()
ap.add_argument("--image", "-i", required=True, help="Image Location")

arguments=vars(ap.parse_args())

image=cv2.imread(arguments["image"])
grayscale_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#Saving the grayscale image for use in pytesseract
cv2.imwrite("tmp.jpg", grayscale_image) 
text = pytesseract.image_to_string(Image.open("tmp.jpg")) 
os.remove("tmp.jpg") 
print(text) 