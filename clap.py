import tkinter as tk
import pyautogui as pag

delay = 100  # Delay between each loop iteration

def toggle():
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
    pag.press("1")
    global loop_id
    loop_id = root.after(delay, loop)  # Run the loop again after 100ms

root = tk.Tk()
root.title('Press Start to start clapping')
toggle_button = tk.Button(root, text='Start', command=toggle, height=20, width=50)
toggle_button.pack()

root.mainloop()
