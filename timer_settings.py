#!/usr/bin/python3

from tkinter import *
from tkinter import font
import configparser

# DEFINITIONS#
win = Tk()
win.title("Timer Settings")
myFont1 = font.Font(family="Helvetica", size=14, weight="bold")
myFont2 = font.Font(family="Helvetica", size=18, weight="bold")

config = configparser.ConfigParser()
config.read("settings.ini")

# VARIABLES
minVal = StringVar(win)
minVal.set(config['SETTINGS']['minutes'])
secVal = StringVar(win)
secVal.set("00")


# FUNCTIONS#
def save():
    # Start the countdown script
    saveButton["text"] = "Click!"


def close():
    win.destroy()  # Close the GUI


# WIDGETS#
spinMin = Spinbox(win, from_=0, to=59, textvariable=minVal, width=3, font=myFont2)
spinMin.grid(row=0, column=0, padx=15, pady=15)

spinSecs = Spinbox(win, from_=0, to=59, textvariable=secVal, width=3, font=myFont2)
spinSecs.grid(row=0, column=1, padx=15, pady=15)

saveButton = Button(win, text="Save", font=myFont1, command=save, height=1, width=5)
saveButton.grid(row=1, column=0, padx=15, pady=15)

closeButton = Button(win, text="Close", font=myFont1, command=close, height=1, width=5)
closeButton.grid(row=1, column=1, padx=15, pady=15)

win.mainloop()

