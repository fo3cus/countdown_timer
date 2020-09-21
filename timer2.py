#!/usr/bin/python3

# Import modules
from tkinter import Tk, ttk, font, StringVar, Menu, Toplevel, Spinbox, Button
import pygame
import configparser
import os
import sys

# Constant reference to file including path
SETTINGS_FILE = os.path.join(sys.path[0], "settings.ini")

# Load the file into config object
config = configparser.ConfigParser()
config.read(SETTINGS_FILE)

# Define variables
iMin = int(config['SETTINGS']['minutes'])
iSec = int(config['SETTINGS']['seconds'])
iTotal = str(iMin) + ":" + str(iSec)
wMin = iMin
wSec = iSec
working = 0

# Start/stop timer
def go_stop():
    global working

    if working == 1:
        working = 0
    else:
        working = 1
        root.after(1000, run_timer)

# Reset timer and update display
def reset():
    global wMin
    global wSec
    global working

    if working == 0:
        # working = 1
        wMin = iMin
        wSec = iSec
        txt.set(iTotal)
        # root.after(1000, run_timer)

# Close all windows
def quit_all():
    root.destroy()

# Run main timer and update display
def run_timer():
    global wMin
    global wSec
    global working

    if working == 1:
        if (wMin == 0) and (wSec == 0):
            txt.set("00:00")
            working = 0
            flash()
            # alarm()
        else:
            txt.set("%02d:%02d" % (wMin, wSec))
            if wSec == 0:
                wMin -= 1
                wSec = 59
            else:
                wSec -= 1
            root.after(1000, run_timer)
    else:
        return

# Play the alarm sound
def alarm():
    pygame.mixer.music.play()

# Flasg displayed numbers
def flash():
    if working == 0:
        current_colour = str(lbl.cget("foreground"))
        if current_colour == "white":
            next_colour = "grey"
        else:
            next_colour = "white"
        lbl.configure(foreground=next_colour)
        root.after(1000, flash)
    else:
        lbl.configure(foreground="white")
        return

# Popup menu on right-click
def popup(event):
    menu.tk_popup(event.x_root, event.y_root)

# Configure settings
def settings():
    global working

    working = 0

    win = Toplevel()
    win.title("Timer Settings")
    my_font1 = font.Font(family="Helvetica", size=14, weight="bold")
    my_font2 = font.Font(family="Helvetica", size=18, weight="bold")

    cfg = configparser.ConfigParser()
    cfg.read(SETTINGS_FILE)

    # Variables
    minute_value = StringVar(win)
    minute_value.set(cfg['SETTINGS']['minutes'])
    second_value = StringVar(win)
    second_value.set(cfg['SETTINGS']['seconds'])

    def save():
        global iMin
        global iSec
        global iTotal

        config_file = open(SETTINGS_FILE, 'w')
        cfg.set('SETTINGS', 'minutes', spin_minutes.get())
        cfg.set('SETTINGS', 'seconds', spin_seconds.get())
        cfg.write(config_file)
        config_file.close()

        iMin = int(spin_minutes.get())
        iSec = int(spin_seconds.get())
        iTotal = str(iMin) + ":" + str(iSec)

        win.destroy()

        reset()

    def close():
        win.destroy()  # Close the GUI

    # WIDGETS#
    spin_minutes = Spinbox(win, from_=0, to=59, textvariable=minute_value, width=3, font=my_font2, state='readonly')
    spin_minutes.grid(row=0, column=0, padx=15, pady=15)

    spin_seconds = Spinbox(win, from_=0, to=59, textvariable=second_value, width=3, font=my_font2, state='readonly')
    spin_seconds.grid(row=0, column=1, padx=15, pady=15)

    win.save_button = Button(win, text="Save", font=my_font1, command=save, height=1, width=5)
    win.save_button.grid(row=1, column=0, padx=15, pady=15)

    win.close_button = Button(win, text="Close", font=my_font1, command=close, height=1, width=5)
    win.close_button.grid(row=1, column=1, padx=15, pady=15)

    win.mainloop()


# --CREATE MAIN DISPLAY-- #
root = Tk()
root.attributes("-fullscreen", True)
root.configure(background='black')
root.config(cursor="none")  # HIDE THE MOUSE CURSOR
root.bind('<x>', quit_all)
root.bind('<F1>', go_stop)
root.bind('<F2>', reset)
root.bind('<F3>', alarm)
root.bind('<Button-3>', popup)

# --INITIALISE THE ALARM SOUND-- #
# pygame.mixer.pre_init(44100, -16, 2, 2048)
# pygame.mixer.init()
# pygame.init()
# pygame.mixer.music.load("tng_red_alert3.mp3")
# pygame.mixer.music.set_volume(10.0)

# --SETUP COUNTER DISPLAY-- #
fnt = font.Font(family='Helvetica', size=300, weight='bold')
txt = StringVar()
lbl = ttk.Label(root, textvariable=txt, font=fnt, foreground="white", background="black")
txt.set(iTotal)
lbl.place(relx=0.5, rely=0.5, anchor="center")

# --MENU-- #
menu_pop = Menu(root)
menu = Menu(menu_pop, tearoff=0)
menu.add_command(label="Start/Stop", accelerator="F1", command=go_stop)
menu.add_command(label="Reset", accelerator="F2", command=reset)
menu.add_separator()
menu.add_command(label="Settings", command=settings)
menu.add_separator()
menu.add_command(label="Exit", accelerator="X", command=quit_all)
menu_pop.add_cascade(label="File", menu=menu)

# --START MAIN LOOP-- #
root.mainloop()
