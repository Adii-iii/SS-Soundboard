import pyautogui
import time
import os
import random
from pynput import keyboard
from playsound import playsound

# Define key combinations and their corresponding sound files
key_sounds = {
    frozenset([keyboard.Key.alt_l, keyboard.KeyCode.from_char('1')]): "media\\sounds\\sicko.mp3",
    frozenset([keyboard.Key.alt_l, keyboard.KeyCode.from_char('2')]): "media\\sounds\\taco gong.mp3",
    frozenset([keyboard.Key.alt_l, keyboard.KeyCode.from_char('3')]): "media\\sounds\\auugh.mp3"
}

# Track pressed keys
pressed_keys = set()


def on_press(key):
    # Add pressed key to the set
    if any([key in comb for comb in key_sounds]):
        pressed_keys.add(key)
    
    # Check if any key combination matches the pressed keys
    for combination in key_sounds:
        if all(k in pressed_keys for k in combination):
            # Play corresponding sound
            sound_file = key_sounds[combination]
            playsound(sound_file)
            break


def on_release(key):
    # Remove released key from the set
    if any([key in comb for comb in key_sounds]):
        pressed_keys.remove(key)
 
    # Stop listener if the Esc key is pressed
    if key == keyboard.Key.esc:
        return False


# Start listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()