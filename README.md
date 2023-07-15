# cosmos-auto-clapper

A very oddly specific program that allows users to clap indefinitely on the app Cosmos , a remote workspace corporate app

Use cases:

Impress your boss by clapping indefinitely when your boss finish talking while you go off for dinner

Annoy your coworkers

## Read this section if you are not a technical person

First open your terminal

If you do not have python installed, type this into your terminal.

### For Mac

```
brew install python3
```

Also install git if you do not have it.

```
brew install git
```

### For Windows

Lookup online LOL im not sure

Once you have python and git installed, type this into your terminal:

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

### For Mac

```
bash run.sh
```

### For Windows (Assuming you have WSL)

```
./run.sh
```

Alternatively, you can install manually

## For people who wants to manually download dependencies/have issues with running bash commands etc.

Install the required dependencies in your terminal

```
pip3 install pyautogui
```

run the following file

```
python3 clap.py
```

Alternatively (or if you failed), you can also do pip install pyautogui and python clap.py

There is going to be a window popup with the "start" button, press the "start" button and make sure that your cosmos is your active window by clicking on your Cosmos window

You can now go off for dinner while you clap for your boss 😎

# Read this if you want to click a clickable file instead of opening the app with the terminal

### For Mac

Open Automator.
Choose Application when it prompts to choose a document type.
In the Actions library, select Utilities and drag Run Shell Script over to the workflow pane.

Type the following:

```
cd /path/to/your/cosmos-auto-clapper
bash run.sh
```

Remember to change the /path/to/your/cosmos-auto-clapper to the actual path where you cloned. For example: /Users/jcjustin/cosmos-auto-clapper if I cloned it into the home directory

If you are facing some error, you can try giving Automator full disk aceess in Settings under "privacy and security", you can also make sure that you have bash.

### For Windows

You can create a batch file that runs your Python script. This will be a .bat file that you can double-click to run.

Here's an example:

Open Notepad.
Type the following command: python C:\path\to\your\script.py.
Save the file with a .bat extension.
Now you can double-click this .bat file to run your Python script.
