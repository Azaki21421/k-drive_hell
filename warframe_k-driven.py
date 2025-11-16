import time
import threading
from pynput import keyboard
from pynput.keyboard import Key, Controller

# --- Configuration ---
TOGGLE_KEY = 'j' or 'J'  # The key to toggle the macro on/off.
SPRINT_KEY = Key.shift  # The key for sprint (Shift)
MOVE_KEY = 'w'  # The key for forward movement (W)

# Global state variables
keyboard_controller = Controller()
running = False
macro_thread = None
lock = threading.Lock()


def toggle_macro():
    """Toggles the state of the macro (on/off)."""
    global running, macro_thread

    with lock:
        # Check if the macro is currently running
        if running:
            running = False
            print("Macro OFF: Keys 'W' and 'Shift' released.")
        else:
            running = True
            print(f"Macro ON: Keys '{MOVE_KEY}' and 'shift' pressed/held. Press '{TOGGLE_KEY}' again to stop.")
            # Start the key-pressing logic in a new thread
            macro_thread = threading.Thread(target=key_press_loop)
            macro_thread.daemon = True  # Allows the main program to exit even if the thread is running
            macro_thread.start()


def key_press_loop():
    """Continuously holds down W and Shift while 'running' is True."""
    global running

    try:
        # 1. Press and HOLD the keys
        keyboard_controller.press(SPRINT_KEY)
        keyboard_controller.press(MOVE_KEY)

        # 2. Loop until the toggle is switched off
        while running:
            # We use a short sleep to prevent the CPU from spinning unnecessarily
            time.sleep(0.1)

    finally:
        # 3. Always ensure keys are released when the loop exits (e.g., when 'running' becomes False)
        keyboard_controller.release(SPRINT_KEY)
        keyboard_controller.release(MOVE_KEY)
        print("Keys released and loop terminated.")


def on_press(key):
    """Callback function for keyboard listener on key press."""
    try:
        if hasattr(key, 'char') and key.char == TOGGLE_KEY:
            toggle_macro()

        # Emergency exit key (Esc)
        if key == Key.esc:
            # Stop listener and release keys if running
            global running
            if running:
                running = False
            return False

    except AttributeError:
        # Ignore keys that don't have a char attribute
        pass
    except Exception as e:
        print(f"An error occurred in on_press: {e}")


def main():
    """Main function to set up and start the keyboard listener."""
    print(f"--- Warframe Auto-Sprint Macro ---")
    print(f"Toggle Key: '{TOGGLE_KEY}' (Press this to start/stop)")
    print(f"Exit Script: Press 'Esc'")
    print(f"Starting listener...")

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

    print("Script terminated.")


if __name__ == "__main__":
    main()