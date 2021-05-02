#!/usr/bin/env bash

VENVNAME=pic_analysis_env 

python3 -m venv $VENVNAME
source $VENVNAME/bin/activate
pip install --upgrade pip

# problems when installing from requirements.txt
pip install ipython
pip install jupyter
pip install matplotlib
pip install opencv-python

python -m ipykernel install --user --name=$VENVNAME

test -f requirements.txt && pip install requirements.txt
python -m spacy download en_core_web_sm

deactivate
echo "build $VENVNAME"