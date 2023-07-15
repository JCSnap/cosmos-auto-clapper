# cosmos-auto-clapper

A very oddly specific program that allows users to clap indefinitely on the app Cosmos , a remote workspace corporate app

Use cases:

Impress your boss by clapping indefinitely when your boss finish taking while you go off for dinner

Annoy your coworkers

## Read this section if you are not a technical person

First open your terminal

If you do not have python installed, type this into your terminal.
For Mac:

```
brew install python3
```

For Windows:
Lookup online LOL im not sure

Once you have python installed, type this into your terminal:

```
git clone https://github.com/JCSnap/cosmos-auto-clapper
```

All the files will be downloaded in your home directory. If you want a specific directory, you can first cd into the directory you want by its path (~ represents the Home directory) by typing this in your terminal (optional)

```
cd ~/Downloads
```

Then clone using the command above

# Using the program

Once you have cloned the directory, go into the directory with the following command in your terminal:

```
cd cosmos-auto-clapper
```

## For people who do not want to deal with installing dependencies

Once you are in the directory,
Run the following if you are using MAC:

```
bash run.sh
```

Or Windows (Assuming you have WSL):

```
./run.sh
```

Alternatively, you can install manually

## For people who wants to manually download dependencies/have issues with running bash commands etc.

```
pip3 install pyautogui
```

## How to use it

Install the required dependencies in your terminal

run the following file

```
python3 clap.py
```

Alternatively (or if you failed), you can also do pip install pyautogui and python clap.py

There is going to be a window popup with the "start" button, press the "start" button and make sure that your cosmos is your active window by clicking on your Cosmos window

You can now go off for dinner while you clap for your boss 😎
