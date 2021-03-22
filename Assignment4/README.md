## INSTRUCTIONS ## 

In order to run the script, please navigate outside the 'Assignment 4' folder and download the whole repository as a .zip file. You can then either upload it to the JupyterHub or run locally on your computer. To do that you should :

1. Open the terminal and navigate to the assignment folder (cd 'your path')
2. Create the virtual environment by typing: ``` bash create_vision_venv.sh ``` (this command will create a new virtual environmnet with all packages specified in the requirements.txt file)
3. Run the python script by typing: ``` python src/lr-mnist.py ``` (by typing -t 'number', where number is any float number brtween 0 and 1 you can secify the test size you wish to work with) 
4. Ryn the second python srript by typing: ``` python src/nn-mnist.py``` (you can specify the test size in the same way as you do in the line above)
