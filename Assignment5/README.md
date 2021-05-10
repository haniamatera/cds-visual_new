## README ##

__Multi-class classification of impressionist painters__


So far in class, we've been working with 'toy' datasets - handwriting, cats, dogs, and so on. However, this course is on the application of computer vision and deep learning to cultural data. This week, your assignment is to use what you've learned so far to build a classifier which can predict artists from paintings.



You can find the data for the assignment here: https://www.kaggle.com/delayedkarma/impressionist-classifier-data



Using this data, you should build a deep learning model using convolutional neural networks which classify paintings by their respective artists. Why might we want to do this? Well, consider the scenario where we have found a new, never-before-seen painting which is claimed to be the artist Renoir. An accurate predictive model could be useful here for art historians and archivists!



For this assignment, you can use the CNN code we looked at in class, such as the ShallowNet architecture or LeNet. You are also welcome to build your own model, if you dare - I recommend against doing this.



Perhaps the most challenging aspect of this assignment will be to get all of the images into format that can be fed into the CNN model. All of the images are of different shapes and sizes, so the first task will be to resize the images to have them be a uniform (smaller) shape.



You'll also need to think about how to get the images into an array for the model and how to extract 'labels' from filenames for use in the classification report

__INSTRUCTIONS__

In order to run the script, please navigate outside the 'Assignment 5' folder and download the whole repository as a .zip file. You can then either upload it to the JupyterHub or run locally on your computer. You can also do that by performing the git clona command (see below). 
Please not thet this folder does not contain data folder. You should therefore have your own data set with all paitings downloaded on your computer and run the code on these files. 


a) Setting up a virtual environment 
```
git clone https://github.com/haniamatera/cds-visual_new.git
cd Assignment5 
bash create_vision_venv.sh
source ./CNN/bin/activate 
```

b) Running the python script 
```
python src/cnn-artists.py -s 'number' 
```

*number stands for the size you wish your paintings to be in a format as follows (x,x) N.B. that the default size is (30,30)

N.B. The output of class_report will be automatically stored in the output folder, along with the lineplot figure showing the training loss accuracy.

```
python covid19.py -h 'number' -w 'number' -e 'number' -s 'number' 

```
