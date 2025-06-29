# 🔐 Task: Simple Keylogger 

## 📌 Task Overview

The objective of this task was to design and implement a **basic keylogger** that records and logs keyboard inputs (keystrokes) and stores them in a file.

This exercise enhances understanding of **keyboard event monitoring**, **file handling**, and emphasizes the importance of **ethical considerations** when working with sensitive system-level operations.

---

## ⚙️ Features

- Monitors and records all keyboard inputs.
- Differentiates between printable characters and special keys (like Enter, Ctrl, Space).
- Logs recorded keys into a local file `key_log.txt`.
- Automatically stops the keylogger when the **ESC key** is pressed.
- Displays a console message indicating that the logger is running.

---

## 📂 Files Included:-

- `keylogger.py` – Python script that implements the keylogger.
- `key_log.txt` – Output file where captured keystrokes are stored.

---

## 🧠 How It Works:-

The script uses the `pynput` Python library to listen for keyboard events:

- `on_press`: Captures every key pressed and writes it to a log file.
  - Printable characters (letters, numbers, space) are written as-is.
  - Special keys (e.g., Enter, Ctrl) are written in brackets: `[Key.enter]`, `[Key.ctrl_l]`, etc.
- `on_release`: Monitors key release events and terminates logging when `Key.esc` is detected.

---

##📋 Sample Output:-
The following is an example output stored in key_log.txt:
```css
hello[Key.space]world[Key.enter]sahil[Key.space]katke[Key.esc]

#✅ How to Run:-
Install pynput:
``bash
pip install pynput

Run the script:
``bash
python keylogger.py

Stop the keylogger:
Press the ESC key on your keyboard.
