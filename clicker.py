from pydoc import cli, text
from tkinter.ttk import Button
from turtle import title
import pyautogui
from time import sleep
def click():
    print(pyautogui.alert(text="This is Auto-Clicker v1, Creator of RubiLom, click OK to continue.", title="Intro", button="ОК"))
    print(pyautogui.alert(text="!To stop the clicker you need to put the mouse in the upper left corner!", title="warning", button="ОК"))
    print(pyautogui.alert(text="You will have 2 seconds to put the cursor where you need it. Click OK when you're ready. The report will start after clicking!", title="warning", button='ОК'))
    pyautogui.PAUSE = 10
    pyautogui.FAILSAFE = True
    pyautogui.click(clicks=1000000, interval=0.05)
    
click()