import os
from tts_func import *

def open_application(input_1):
    if "chrome" in input_1:
        assistant_speaks("Opening Google Chrome")
        os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
        return

    elif "firefox" in input_1 or "mozilla" in input_1:
        assistant_speaks("Opening Mozilla Firefox")
        os.startfile("C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe")
        return

    elif "word" in input_1:
        assistant_speaks("Opening Microsoft Word")
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\\Word 2013.lnk')
        return

    elif "excel" in input_1:
        assistant_speaks("Opening Microsoft Excel")
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\\Excel 2013.lnk')
        return

    elif "power point" in input_1:
        assistant_speaks("Opening Microsoft Power Point")
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\\PowerPoint 2013.lnk')
        return

    elif "settings" in input_1:
        assistant_speaks("Opening Microsoft Excel")
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\\Settings.lnk')
        return

    elif "notepad++" in input_1:
        assistant_speaks("Opening Microsoft Excel")
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\\Notepad++.lnk')
        return

    elif "task manager" in input_1:
        assistant_speaks("Opening Microsoft Excel")
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\System Tools\\Task Manager.lnk')
        return

    else:
        assistant_speaks("Application not available")
        return
