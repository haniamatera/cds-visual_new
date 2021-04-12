########____Assignment5____########
###__Art classification model__###


#importing libraries 
import os
import numpy as np 
import sys
sys.path.append(os.path.join(".."))
import cv2
import glob
import matplotlib.pyplot as plt
import pydot
import graphviz
import pandas as pd
import argparse


# sklearn tools
from sklearn.preprocessing import LabelBinarizer
from sklearn.metrics import classification_report

# tf tools
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import (Conv2D, 
                                     MaxPooling2D, 
                                     Activation, 
                                     Flatten, 
                                     Dense)
from tensorflow.keras.utils import plot_model
from tensorflow.keras.optimizers import SGD
from tensorflow.keras import backend as K



#defining function for later use 

def plot_history(H, epochs):
    # visualize performance
    plt.style.use("fivethirtyeight")
    plt.figure()
    plt.plot(np.arange(0, epochs), H.history["loss"], label="train_loss")
    plt.plot(np.arange(0, epochs), H.history["val_loss"], label="val_loss")
    plt.plot(np.arange(0, epochs), H.history["accuracy"], label="train_acc")
    plt.plot(np.arange(0, epochs), H.history["val_accuracy"], label="val_acc")
    plt.title("Training Loss and Accuracy")
    plt.xlabel("Epoch #")
    plt.ylabel("Loss/Accuracy")
    plt.legend()
    plt.tight_layout()
    plt.savefig("output/plot_training_loss_accuracy.jpg")



#defining main function 

def main(args):
    
    image_size = args["image_size"]  #image size specified in the terminal 

    #extracting the labels of all pictures - artists names
    artists_path = os.path.join("data","training","training")
    artists = os.listdir(artists_path)
    artists=sorted(artists)

    # initialising empty lists 
    train_paintings= []  #trainX ~ list of paintings from the training set 
    train_paintings_artist=[] #trainY ~ list of labels of the training set 
    test_paintings= []  #testX ~ list  of paintings from teh testing set 
    test_paintings_artist=[]   #testY  ~ list of labels from the testing set 
    
    trainX_resized=[]
    testX_resized=[]
    

    #fetching the data from the folders :
    for artist in artists:
        #train :
        for train_painting in glob.glob(os.path.join("data","training","training",f"{artist}","*.jpg")):
            train_paintings_artist.append(artist)
            train_paintings.append(cv2.imread(train_painting))
        #test :
        for test_painting in glob.glob(os.path.join("data","validation","validation",f"{artist}","*.jpg")):
            test_paintings_artist.append(artist)
            test_paintings.append(cv2.imread(test_painting))
        
               
    #resizing images
    
    #train
    for painting in train_paintings:
        resized=cv2.resize(painting,image_size,interpolation=cv2.INTER_AREA)
        #normalize:
        resized = resized.astype("float")/ 255.
        trainX_resized.append(resized)

    #test
    for painting in test_paintings:
        resized=cv2.resize(painting,image_size,interpolation=cv2.INTER_AREA)
        #normalize:
        resized = resized.astype("float")/ 255.
        testX_resized.append(resized)
    
    
    #renaming 
    trainX_len = len(trainX_resized)
    testX_len = len(testX_resized)
    
    #changing into an array and reshapig 
    trainX_resized=np.array(trainX_resized).reshape(trainX_len,30,30,3)
    testX_resized=np.array(testX_resized).reshape(testX_len,30,30,3)
    
    
    # integers to one-hot vectors so that they are binarized
    lb = LabelBinarizer()
    trainY = lb.fit_transform(train_paintings_artist)
    testY = lb.fit_transform(test_paintings_artist) 
    
   
    ###BUILDING  THE MODEL###
    # initialise model
    model = Sequential()

    # define CONV => RELU layer
    model.add(Conv2D(30, (3, 3), 
                 padding="same", 
                 input_shape=(30, 30, 3)))
    model.add(Activation("relu"))

    # softmax classifier
    model.add(Flatten())
    model.add(Dense(10))
    model.add(Activation("softmax"))
    
    
    #compiling the model 
    opt = SGD(lr =.01) #from 0.001 to 0.01
    model.compile(loss="categorical_crossentropy",
              optimizer=opt,
              metrics=["accuracy"])
    
    #training the model 
    H = model.fit(trainX_resized, trainY, 
              validation_data=(testX_resized, testY), 
              batch_size=100,
              epochs=40,
              verbose=1)
    
    #predictions 
    predictions = model.predict(testX_resized, batch_size=32)
    
    
    #generating the classifiation report
    class_report= pd.DataFrame(classification_report(testY.argmax(axis=1),
                            predictions.argmax(axis=1),
                            target_names=artists,
                            output_dict =True))
    
    print(class_report)

    #saving class_report as a csv file in the output folder
    class_report.to_csv("output/class_report.csv", sep=",")

    #saving the performance plot as an img in the output folder 
    plot_history(H,40)
    
     
    
if __name__=="__main__":
    
    #creating a parser
    ap = argparse.ArgumentParser(description = "Creating a classification model")
    #argument -t for specifying the text size
    ap.add_argument("-s","--image_size", help ="please provide a desired image size. The defaule one is (30,30)", default= (30,30), type = float)
    
    args = vars(ap.parse_args())
  

    main(args)