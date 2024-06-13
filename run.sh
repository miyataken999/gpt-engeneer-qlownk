#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Run the main script with the video ID as an argument
python src/main.py $1
