__INSTRUCTIONS__


In order to run the script, it is necessary to create a virtual environment containing all the packages needed to run the script created for this assignment. That can be done by executing the git ```clone command``` and pasting the path to the assignment folder, running the bash script to create the environment and activating it. In order to do that, the following commands need to be executed:

```
git clone https://github.com/haniamatera/cds-visual_new.git
cd Assignment2
bash create_vision_venv.sh
source ./image_search_env/bin/activate 

```
Once the data is downloaded and the virtual environment is created, the .py script can be run in the terminal where additional parameters such as -f (file path: a path to the images that the target image will be compared to) and -t (target image an image of your individual choice) can be specified:

```
python image_search.py -f data/*.jpg -t  data/image_0006.jpg

```
