#!/bin/bash

# You might not have bash if you are using Windows.
source ~/.bash_profile

# Define your dependency
DEPENDENCY="pyautogui"

# Function to check if a command exists
command_exists () {
    type "$1" &> /dev/null ;
}

# Function to install the dependency and run the script with given pip and python commands
run_with_python () {
    PIP_CMD=$1
    PYTHON_CMD=$2

    # Check if the commands are installed
    if ! command_exists $PIP_CMD; then
        echo "Error: $PIP_CMD not found. Please install it and try again."
        exit 1
    fi

    if ! command_exists $PYTHON_CMD; then
        echo "Error: $PYTHON_CMD not found. Please install it and try again."
        exit 1
    fi

    # Check if the dependency is installed
    $PIP_CMD show $DEPENDENCY > /dev/null 2>&1

    # If the dependency is not installed
    if [ $? -ne 0 ]; then
        echo "The dependency $DEPENDENCY is not installed."
        echo "Installing $DEPENDENCY..."
        $PIP_CMD install $DEPENDENCY
        if [ $? -ne 0 ]; then
            return 1
        fi
    fi

    # Run your python script
    $PYTHON_CMD clap.py
    if [ $? -ne 0 ]; then
        return 1
    fi

    return 0
}

run_with_python pip python
if [ $? -ne 0 ]; then
    echo "Failed to run with pip and python. Trying with pip3 and python3..."
    run_with_python pip3 python3
    if [ $? -ne 0 ]; then
        echo "Failed to run with pip3 and python3."
    fi
fi
