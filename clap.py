import tkinter as tk
import pyautogui as pag

delay = 100  # Delay between each clap (1000 = 1 second)
key_to_press = "1"

# Mapping for button titles
button_titles = {
    "1": "👏",
    "2": "🎉",
    "3": "👍",
    "4": "🙌",
    "5": "🤣",
    "6": "🧡",
    "7": "😢",
    "8": "😱",
    "9": "👋",
    "t": "❄️",
    "all": "All",
}

def toggle(event=None):
    # Check if the loop is currently running
    if 'loop_id' in globals():
        # If it is, cancel it and delete the reference
        root.after_cancel(loop_id)
        del globals()['loop_id']
        toggle_button.config(text='Start')
    else:
        # If it's not running, start it
        loop()
        toggle_button.config(text='Stop')

def loop():
    global loop_id
    if key_to_press == "all":
        for i in range(1, 10):
            pag.press(str(i), interval=0.01)
    else:
        pag.press(key_to_press)
    loop_id = root.after(delay, loop)  # Run the loop again after 100ms

def open_settings():
    # Create a new window
    global settings_window
    settings_window = tk.Toplevel(root)
    settings_window.title('Settings')

    # Create buttons for each key to press
    for key, title in button_titles.items():
        button = tk.Button(settings_window, text=title, command=lambda key=key: set_key(key))
        button.pack(side="left")

def set_key(key):
    global key_to_press
    key_to_press = key
    print(f"Set key to press to: {key_to_press}")
    # If a settings window is currently open, hide it
    if 'settings_window' in globals():
        settings_window.withdraw()
    # If the loop is currently running, stop it
    if 'loop_id' in globals():
        root.after_cancel(loop_id)
        del globals()['loop_id']
        toggle_button.config(text='Start')

root = tk.Tk()
root.title('Press Start to start clapping')
toggle_button = tk.Button(root, text='Start', command=toggle, height=20, width=50)
toggle_button.pack()
settings_button = tk.Button(root, text='Settings', command=open_settings)
settings_button.pack()

# Press space bar to stop
root.bind_all('<space>', toggle)

root.mainloop()
