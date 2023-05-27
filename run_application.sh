#!/bin/bash
cd ./src
if [[ -x "$(command -v python3)"]]
then
    pyv="$(python -V 2>&1)"
    if [[ $pyv == "Python 3"* ]]
    then
      echo "You have the correct version of Python installed."
    else
      echo "You have an outdated version of Python installed. Please update Python" >&2
    fi
else
  echo "You don't have Python installed in your system. Please install Python to run this application!" >&2
fi
echo "First, I will create a virtual environment using the name .venv"
python3 -m venv .venv
echo "Now, I will install all of the dependencies required for this application:"
pip install -r ./requirements.txt
echo "Now, we will run the python file for the application."
python3 ./main.py
deactivate