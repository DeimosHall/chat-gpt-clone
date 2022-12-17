#!/bin/bash

sudo apt install python3-pip
mkdir env
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
pip list