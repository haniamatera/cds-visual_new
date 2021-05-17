## README ##

__Multi-class classification of impressionist painters__


__INSTRUCTIONS__

In order to run the script, please navigate outside the 'Assignment 5' folder and download the whole repository as a .zip file. You can then either upload it to the JupyterHub or run locally on your computer. You can also do that by performing the ```-git clone``` command (see below). 
Please note that this folder does not contain the data folder. You should therefore have your own data set with all paitings downloaded on your computer and run the code on these files. 


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


