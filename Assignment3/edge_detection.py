#ASSIGNMENT 3- EDGE DETECTION


####Tasks:

#- Draw a green rectangular box to show a region of interest (ROI) around the main body of text in the middle of the image. Save this as image_with_ROI.jpg.
#- Crop the original image to create a new image containing only the ROI in the rectangle. Save this as image_cropped.jpg.
#- Using this cropped image, use Canny edge detection to 'find' every letter in the image
#- Draw a green contour around each letter in the cropped image. Save this as image_letters.jpg



#importing necessary packages 
import os
import sys
sys.path.append(os.path.join(".."))
import cv2
import numpy as np
import glob
import matplotlib as mpl
import matplotlib.pyplot as plt
from pathlib import Path
import csv   
  
    
 # loading the image 
file_path= os.path.join ("images/image.jpeg")
image= cv2.imread(file_path)


##TASK1
#specifying the frame of the area of interest (ROI)
upper_left =(1385,880) # specyfying corners of the picture (specific pixels)
bottom_right =(2890,2800) 
color = (0, 255, 0)
thickness = 4

#drawing a rectangular AOI on the picture
image_ROI=cv2.rectangle(image.copy(), upper_left, bottom_right, color, thickness)


#saving the image in the 'images' folder
filename="images/image_with_ROI.jpg"
cv2.imwrite(filename,image_ROI)


#TASK2
#cropping 
image_cropped = image[upper_left[1]:bottom_right[1],upper_left[0]:bottom_right[0]] # cropping the image based on the AOI specified above


#saving the new image to the images folder
filename2="images/image_cropped.jpg"
cv2.imwrite(filename2,image_cropped)


#TASK 3 : Canny
#first of all, I am changing the image to grey 
grey_image = cv2.cvtColor(image_cropped,cv2.COLOR_BGR2GRAY)


# we need to blur it 
blurred= cv2.GaussianBlur(grey_image,(5,5),0)

#applying canny to the blurred image 
canny = cv2.Canny(blurred, 100,150)


#Task 4 
#drawing green contours of the letters 
#specifying the countours 
(contours,_) = cv2.findContours(canny.copy(),
                 cv2.RETR_EXTERNAL, 
                 cv2.CHAIN_APPROX_SIMPLE)


#creating an image with the letter outline
letters= cv2.drawContours(image_cropped.copy(), # draw contours on original image
                        contours,      # our list contours
                        -1,            # which contours to draw
                        (220,255,0),     # contour colour 
                        2)           # contour pixel width 

#saving the image to the images folder 
filename3="images/image_letters.jpg"
cv2.imwrite(filename3,letters)
