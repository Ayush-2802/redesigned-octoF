# Keyboard module in Python 
import keyboard 

def execute():
    print("hotkey")
# press a to print rk  
keyboard.add_hotkey('windows + shift + f', execute()) 

keyboard.wait('esc') 
