#!/bin/bash
cd ./src;
if [[ -x "$(command -v python3)" ]]
then
  pyv="$(python -V 2>&1)"
  if [[ $pyv == "Python 3.11"* ]]
  then
    echo "The correct version of Python is installed. Let's continue!"
  else
    echo "The version of Python installed is an outdated version. Please update to the latest version of Python." >&2
  fi
else
  echo "Python is not installed in your system. Please install Python version 3 (at least) to run this application!" >&2
fi
echo "First, I will create a virtual environment using the name .venv and activate it"
python3 -m venv .venv
source .venv/bin/activate
echo "Now, I will install all dependencies required for the application to run smoothly."
pip install -r ./requirements.txt
echo "And finally, I will run the python file for the application."
python3 ./main.py 
deactivate