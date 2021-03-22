#____NEURAL NETWORK___#

#importing necessary packages 
#path tools 
import sys,os
sys.path.append(os.path.join(".."))

#neural networks with numpy
from utils.neuralnetwork import NeuralNetwork


from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn import datasets
import argparse


def main(args):
    
    test_size = args["test_size"]
    layers= args["layers"]
    
    #loading data
    digits = datasets.load_digits()

    #converting to float numbers 
    data = digits.data.astype("float")

    # MinMax regularization
    data = (data - data.min())/(data.max() - data.min())

    # split data
    X_train, X_test, y_train, y_test = train_test_split(data, 
                                                  digits.target, 
                                                  test_size=0.2)


    # convert labels from integers to vectors
    y_train = LabelBinarizer().fit_transform(y_train)
    y_test = LabelBinarizer().fit_transform(y_test)

    
    
    # train network
    print("[INFO] training network...")
    
    if (len(layers)==1):
        nn=NeuralNetwork([X_train.shape[1],layers[0],10])
    elif (len(layers)==2):
        nn=NeuralNetwork([X_train.shape[1],layers[0],layers[1],10])
    elif (len(layers)==2):
        nn=NeuralNetwork([X_train.shape[1],layers[0],layers[1],layers[2],10])
    else:
        nn= NeuralNetwork([X_train.shape[1],10])
    
    print("[INFO] {}".format(nn))
    nn.fit(X_train, y_train, epochs=1000)

    # evaluate network
    print(["[INFO] evaluating network..."])
    predictions = nn.predict(X_test)
    predictions = predictions.argmax(axis=1)
    print(classification_report(y_test.argmax(axis=1), predictions))
    
    
if __name__=="__main__":
    
    #parser
    ap = argparse.ArgumentParser(description = "Training a neural network")
    #parser.add_argument("--l","--layers", nargs="+")

 
    ap.add_argument("-t","--test_size", help ="please provide a desired data test size", default= 0.25, type = float)
    ap.add_argument("-l","--layers",default=[],type= int) 
    ap.add_argument("--epochs",default=1000,type= int)
    
    args = vars(ap.parse_args())
  

    main(args)
   