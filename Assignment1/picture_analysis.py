###____Assignment1_____###

### Picture Analysis ###


#importing necessary packages 
import os
import numpy as np # creating an abbreviation to save keystrokes
import pandas as pd
import cv2
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from pathlib import Path


#defining the function needed to split the image 

def image_split(h1, h2, w1, w2, image):
    new_image = image[h1:h2, w1:w2]

    return(new_image)


#defining the filepath 
data_path = os.path.join("data")


# define pandas with appropriate column names
Columns = ['filename','width','height']           
DATA = pd.DataFrame(columns = Columns)

# Create a list of all filenames in the image folder.
filelist = []
basepath = Path(data_path)
files_in_basepath = basepath.iterdir()
for item in files_in_basepath:
    if item.is_file():
        filelist.append(item.name)
        
        
#defining a loop which slices images, saves them separately in a new folder and creates a data frame containing information about their properties (such as height, width and number of channels)       
        
for filename in filelist:
    
    # Create a specific image path and import&read the image
    img_path = os.path.join(data_path, filename)
    image = cv2.imread(img_path)
    
    # Assign respective properties of the image to variables 
    height, width, channels = image.shape
    
    # New heights and widths (N.B. int() is neccessary here)
    new_height = int(height/2)
    new_width = int(width/2)
    
    # Creating split images
    top_left = image_split(0,new_height,0,new_width,image)
    top_right = image_split(0,new_height,new_width, width,image)
    bottom_left = image_split(new_height,height,0, new_width,image)
    bottom_right = image_split(new_height,height,new_width, width,image)

    # collect the 4 image objects in a string
    new_images = [top_left, top_right,bottom_left, bottom_right]
    
    # Loop over each of the 4 split images generated from one image, save them, and put them into to the dataframe
    img_count = 1 
    
    for img in new_images:
    
        # Generate unique filename
        new_filename = filename [:-4] + "_slice" + str(img_count) + ".jpg"
    
        # save the split image
        outfile = os.path.join("new_img", new_filename) # joining filepath and new filename.
        cv2.imwrite(outfile, img)
    
        # Save to dataframe
        DATA = DATA.append({
            'filename': new_filename,
            'height': new_height,
            'width': new_width
            }, ignore_index=True) 
    
        img_count = img_count + 1

# Save the dataframe as a csv file
DATA.to_csv("image_data.csv")
                        
                        
                        