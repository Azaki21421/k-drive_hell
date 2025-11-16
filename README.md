# Warframe K-Drive Macro for 'K-Driven' Achievement
A simple, lightweight Python script designed to automate the perpetual **Sprint + Forward Movement** key combination (Shift + W) specifically for **K-Drive** movement in Warframe. This macro can assist users targeting the **'K-Driven' achievement** by simplifying long-distance travel.

# ⚠️ Disclaimer: Use at Your Own Risk
**By downloading and running this script, you acknowledge that you use it entirely at your own risk.**

The use of automation tools and macros may violate the Terms of Service or End-User License Agreement (EULA) of certain games, including Warframe. Digital Extremes (Warframe's developer) generally discourages the use of third-party tools that automate gameplay. While this macro is simple and only simulates basic keystrokes, it is the user's sole responsibility to ensure compliance with all applicable game rules and policies. The author of this script assumes no responsibility for any actions taken against your account.

# Features
- **Single-Key Toggle:** Press j to start the macro (press and hold 'W' and 'Shift'). Press j again to stop it (release 'W' and 'Shift').

- **Persistent Movement:** Uses a separate thread to maintain key pressure, ensuring reliable movement until manually stopped.

- **Emergency Exit:** Press the Esc key at any time to immediately stop the macro, release all keys, and close the script.

# Prerequisites

1. **Install Python:** Ensure you have a recent version of Python 3 installed on your system.

2. **Install** ```pynput```: Open your command line or terminal and run the following command to install the required library:
   ```pip install pynput``` 
   Or simply use ```requirements.txt``` to install the required library:
   ```pip install -r requirements.txt```


# How to Run

1. Download provided script or (if i do) .exe app.

2. Open your command line or terminal.

3. Run the script:
   ```python warframe_k-driven.py```
4. Once the script is running, switch to Warframe, summon your K-Drive, and press the toggle key.

# Usage

|Action|Key|Result|
|------|---|------|
|Start Macro|```j```|Holds down 'W' and 'Shift' simultaneously (K-Drive turbo/sprint).|
|Stop Macro|```j```|Releases 'W' and 'Shift', stopping the auto-run.|
|Exit Script|```Esc```|Immediately shuts down the Python script.|

# Configuration

You can easily modify which keys are used by editing the variables at the top of the ```warframe_k-driven.py``` file:
```
# --- Configuration ---
# 1. TOGGLE_KEY: The key to press to start the auto-sprint and press again to stop it.
TOGGLE_KEY = 'j'  

# 2. SPRINT_KEY: Must use the pynput Key enum for special keys like Shift, Ctrl, Alt, etc.
SPRINT_KEY = Key.shift

# 3. MOVE_KEY: The key for forward movement.
MOVE_KEY = 'w'
```
## Notes on Configuration:

- **Special Keys:** For keys like ```Shift```, ```Ctrl```, ```Alt```, and ```Enter```, you must use the format ```Key.keyname``` (e.g., ```Key.shift```, ```Key.ctrl```).

- **Standard Keys:** For alphanumeric keys (like ```w```, ```j```, ```k```), use the character in single quotes (e.g., ```'w'```).

# TODO:

- ```*.EXE``` app for simpler use
