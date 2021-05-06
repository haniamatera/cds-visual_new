## INSTRUCTIONS ## 

In order to run the script, please navigate outside the 'Assignment 4' folder and download the whole repository as a .zip file. You can then either upload it to the JupyterHub or run locally on your computer. You can also use the ```-git clone``` command. You can do it as follows: 

1. Setting up the virtual environment:
```
git clone https://github.com/haniamatera/cds-visual_new.git
cd Assignment4
bash create_vision_venv.sh
source ./classification_environment/bin/activate 
```

2. Running the logistic regression python script 
```
python src/lr-mnist.py -t 'number'

``` 
*number is any float number brtween 0 and 1 you can secify the test size you wish to work with


3. Running the second neural network python srript
``` 
python src/nn-mnist.py -t 'number'

```
*similarly, you can specify the desired test size (-t) in the same way as you do in the line above
