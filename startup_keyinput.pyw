from pynput.keyboard import Key, KeyCode, Listener
import os

def function_1():
    os.startfile('D:\\My Creation\\programms\\FRIDAY\\main.py')    

# Createing a mapping of keys to function (use frozenset as sets are not hashable - so they can't be used as keys)
combination_to_function = {
    frozenset([Key.shift, KeyCode(char='f')]): function_1, # No `()` after function_1 because we want to pass the function, not the value of the function
    frozenset([Key.shift, KeyCode(char='F')]): function_1,
}

# Currently pressed keys
current_keys = set()

def on_press(key):
    # When a key is pressed, adding it to the set we are keeping track of and check if this set is in the dictionary
    current_keys.add(key)
    if frozenset(current_keys) in combination_to_function:
        # If the current set of keys are in the mapping, execute the function
        combination_to_function[frozenset(current_keys)]()

def on_release(key):
    # When a key is released, removeing it from the set of keys we are keeping track of
    current_keys.remove(key)

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
