#____Assignment4_____#
#building logistic regression classifier 

#importing necessary packages 

import os
import sys
import argparse
sys.path.append(os.path.join(".."))

# Import teaching utils
import numpy as np
import utils.classifier_utils as clf_util

# Import sklearn metrics
from sklearn import metrics
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score



#defining main function 
def main(args):
    
    #assigning text_size to the text size specified in the command line 
    test_size = args["test_size"]
    
    #fetching data
    X, y = fetch_openml('mnist_784', version=1, return_X_y = True) 
    #x is a list of pixels  and y is a label
    
    #changing x and y to arrays 
    X = np.array(X)
    y = np.array(y)
    
    #predefining classes
    classes = sorted(set(y))
    nclasses = len(classes)
    
    #creating a training data set 
    X_train, X_test, y_train, y_test = train_test_split(X, 
                                                    y, 
                                                    random_state = 9, 
                                                    test_size = test_size)
    
    #scaling the features
    X_train_scaled = X_train/255.0
    X_test_scaled = X_test/255.0
    
    
    #training the model
    clf = LogisticRegression(penalty='none', 
                         tol=0.1, 
                         solver='saga',
                         multi_class='multinomial').fit(X_train_scaled, y_train)
    
   

    y_pred = clf.predict(X_test_scaled)
    
    
    #predicting the accuracy 
    accuracy = accuracy_score(y_test, y_pred)
    
    #confusion matrix
    cm = metrics.classification_report(y_test, y_pred)
    
    print(cm)#printing the accuracy in the terminal



    
if __name__=="__main__":
    
    #creating a parser
    ap = argparse.ArgumentParser(description = "Training a model")
    #argument -t for specifying the text size
    ap.add_argument("-t","--test_size", help ="please provide a desired data test size", default= 0.25, type = float)
    
    args = vars(ap.parse_args())
  

    main(args)