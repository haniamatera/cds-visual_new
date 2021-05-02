###____Assignment2____###
###___Image search___###


#Importing necessary packages 
import os
import sys
sys.path.append(os.path.join(".."))
import cv2
from pathlib import Path
import csv


# Import libraries
import os, glob, sys, argparse, cv2
import pandas as pd
import numpy as np


# Defining the main function with arguments: targetpath- path to a target image and filepath- a path to the images which the target image will be compared to 

def main(targetpath, filepath):
    
    # Empty lists for appending
    filenames = []
    distance_to_image_selected = [] #the selected image is: image_0006.jpg

    # Target image histogram, normalized
    target_image = cv2.imread(targetpath)
    target_hist = cv2.calcHist([target_image], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    target_hist = cv2.normalize(target_hist, target_hist, 0,255, cv2.NORM_MINMAX)
    
    # For each of the non-target files, get filename and calculate distance to target
    for file in glob.glob(filepath):
        # Get filename
        filename = os.path.split(file)[1]
        filenames.append(filename)

        # Read image, and calculate hist distance
        img = cv2.imread(file)
        hist = cv2.calcHist([img], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
        hist = cv2.normalize(hist, hist, 0,255, cv2.NORM_MINMAX)
        dist_to_target = round(cv2.compareHist(target_hist, hist, cv2.HISTCMP_CHISQR), 2)
        distance_to_image_selected.append(dist_to_target)
    
    # Create a df with the information on distances
    df = pd.DataFrame(list(zip(filenames, distance_to_image_selected)), 
                columns =['filename', 'dist_to_target'])
    
    # Create outpath for df
    target_image_filename = os.path.split(targetpath)[1][:-4] + f"_rgb_distances.csv"
    outfilepath = os.path.join("output", target_image_filename)

    # Save df
    df.to_csv(outfilepath, index = False)
    print(f"A new file has been created succesfully: \"{outfilepath}\"")

# Define behaviour when called from command line
if __name__=="__main__":
    # Initialise ArgumentParser class
    parser = argparse.ArgumentParser(description = "Calculates distance from a target image, to a set of images within a folder")
    
    # Add inpath argument
    parser.add_argument(
        "-f",
        "--filepath", 
        type = str,
        default = os.path.join("data", "*.jpg"),
        required = False,
        help= "str - path to files from which to calculate distance to target image")
    
    # Add outpath argument
    parser.add_argument(
        "-t",
        "--targetpath",
        type = str, 
        default = os.path.join("data", "image_0006.jpg"),
        required = False,
        help = "str - path to target file, from which to calculate distance to the other images")
    
    # Taking all the arguments we added to the parser and input into "args"
    args = parser.parse_args()

    main(args.targetpath, args.filepath)