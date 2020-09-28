#!/usr/bin/python3

# TODO: add my details and docstrings etc

# Import modules
from tkinter import Tk, font, ttk, StringVar, Menu, Toplevel, Spinbox, Button
import pygame
import configparser
import os
import sys
import time

# Constant reference to file including path
SETTINGS_FILE = os.path.join(sys.path[0], "settings.ini")

class timer():
    # Load the file into config object
    config = configparser.ConfigParser()
    config.read(SETTINGS_FILE)

    # TODO: this could be a class?
    # Define variables
    iMin = int(config['SETTINGS']['minutes'])
    iSec = int(config['SETTINGS']['seconds'])
    iTotal = str(f'{iMin:02}') + ":" + str(f'{iSec:02}') # Format loaded numbers with leading zeroes
    wMin = iMin
    wSec = iSec
    working = 0

    # Create main display
    root = Tk()
    root.attributes("-fullscreen", True)
    root.configure(background='black')
    # root.config(cursor="none")  # Hide the mouse cursor
    root.bind('<x>', quit_all)
    root.bind('<F1>', go_stop)
    root.bind('<F2>', reset)
    root.bind('<F3>', alarm)
    root.bind('<Button-3>', popup)

    # # Initialise the alarm sound
    # pygame.mixer.pre_init(44100, -16, 2, 2048)
    # pygame.mixer.init()
    # pygame.mixer.music.load("tng_red_alert3.mp3")
    # pygame.mixer.music.set_volume(10.0)

    # Set up counter display
    fnt = font.Font(family='Helvetica', size=300, weight='bold')
    txt = StringVar()
    lbl = ttk.Label(root, textvariable=txt, font=fnt, foreground="white", background="black")
    txt.set(iTotal)
    lbl.place(relx=0.5, rely=0.5, anchor="center")

    # Menu
    menu_pop = Menu(root)
    menu = Menu(menu_pop, tearoff=0)
    menu.config(bg="black", fg="white", relief="raised")
    menu.add_command(label="Start/Stop", accelerator="F1", command=go_stop)
    menu.add_command(label="Reset", accelerator="F2", command=reset)
    menu.add_separator()
    menu.add_command(label="Settings", command=settings)
    menu.add_separator()
    menu.add_command(label="Exit", accelerator="X", command=quit_all)
    menu_pop.add_cascade(label="File", menu=menu)

    # Start/stop timer
    def go_stop(self, *args):
        if self.working == 1:
            self.working = 0
        else:
            self.working = 1
            self.root.after(500, self.run_timer)  # Queue function to execute after 0.5 seconds

    # Reset timer and update display, only works if currently stopped
    def reset(self, *args):
        # Pull in global variables so they can be changed locally
        if self.working==1 and self.wMin==0 and self.wSec==0:
            self.working = 0

        if self.working == 0:
            self.wMin = self.iMin
            self.wSec = self.iSec
            self.txt.set(self.iTotal)

    # Close all windows
    def quit_all(self, *args):
        self.root.destroy()

    # Run main timer and update display
    def run_timer(self):
        # Pull in global variables so they can be changed locally
        if self.working == 1:
            if self.wMin==0 and self.wSec==0:
                self.txt.set("00:00")
                self.flash()
                # alarm()
            else:
                self.txt.set("%02d:%02d" % (self.wMin, self.wSec))
                if self.wSec == 0:
                    self.wMin -= 1
                    self.wSec = 59
                else:
                    self.wSec -= 1
                self.root.after(1000, self.run_timer)
        else:
            return

    # Play the alarm sound
    def alarm(self):
        pygame.mixer.music.play()

    # Flash displayed numbers
    def flash(self):
        if self.working == 1:
            current_colour = str(self.lbl.cget("foreground"))
            if current_colour == "white":
                next_colour = "grey"
            else:
                next_colour = "white"
            self.lbl.configure(foreground=next_colour)
            self.root.after(1000, self.flash)
        else:
            self.lbl.configure(foreground="white")
            return

    # Popup menu on right-click
    def popup(self, event):
        self.menu.tk_popup(event.x_root, event.y_root)

    # Start main loop
    root.mainloop()

main_timer = timer

# TODO: this could be a class?
# Configure settings window
class settings():
    timer.working = 0

    win = Toplevel()
    win.title("Settings")
    win.config(bg="black", bd="1", relief="flat")
    win.resizable(height=False, width=False)
    my_font1 = font.Font(family="Helvetica", size=12, weight="normal")
    my_font2 = font.Font(family="Helvetica", size=18, weight="bold")

    cfg = configparser.ConfigParser()
    cfg.read(SETTINGS_FILE)

    # Variables
    minute_value = StringVar(win)
    minute_value.set(cfg['SETTINGS']['minutes'])
    second_value = StringVar(win)
    second_value.set(cfg['SETTINGS']['seconds'])

    # Widgets
    spinput = win.register(validate_numbers)
    spin_minutes = Spinbox(
            win,  # Window element is assigned to
            validate="key",  # Validate on key press
            validatecommand=(spinput, "%P", "%s"),  # Execute this command to validate
            from_=0,  # Minimum value when using arrows
            to=59,  # Maximum value when using arrows
            textvariable=minute_value,  # Set initial value
            bg="black",  # Background colour
            relief="flat",  # Border design
            fg="white",  # Text colour
            bd=1,  # Border width in pixels
            width=3,  # Width of spinbox entry in characters
            font=my_font2,  # Font for text
            justify="center"  # Alignment of text in element
        )
    spin_minutes.grid(row=0, column=0, padx=10, pady=10)  # Layout in window

    spin_seconds = Spinbox(
            win,
            validate="key",
            validatecommand=(spinput, "%P", "%s"),
            from_=0,
            to=59,
            textvariable=second_value,
            bg="black",
            relief="flat",
            fg="white",
            bd=1,
            width=3,
            font=my_font2,
            justify="center"
        )
    spin_seconds.grid(row=0, column=1, padx=10, pady=10)

    win.save_button = Button(
            win,
            text="Save",
            command=save,
            font=my_font1,
            bg="black",
            relief="flat",
            fg="white",
            bd=1,
            width=5,
            justify="center",
            padx=5,
            pady=5
        )
    win.save_button.grid(row=1, column=0, padx=10, pady=10)

    win.close_button = Button(
            win,
            text="Close",
            command=close,
            font=my_font1,
            bg="black",
            relief="flat",
            fg="white",
            bd=1,
            width=5,
            justify="center",
            padx=5,
            pady=5
        )
    win.close_button.grid(row=1, column=1, padx=10, pady=10)

    def save(self):
        global iMin
        global iSec
        global iTotal

        if spin_minutes.get() == '':
            iMin = 0
        else:
            iMin = int(spin_minutes.get())

        if spin_seconds.get() == '':
            iSec = 0
        else:
            iSec = int(spin_seconds.get())

        config_file = open(SETTINGS_FILE, 'w')
        cfg.set('SETTINGS', 'minutes', str(iMin))
        cfg.set('SETTINGS', 'seconds', str(iSec))
        cfg.write(config_file)
        config_file.close()

        iTotal = str(f'{iMin:02}') + ":" + str(f'{iSec:02}')

        self.win.destroy()

        reset()

    def close(self):
        self.win.destroy()  # Close the GUI


    # Validate input and disallow anything but numbers and empty
    def validate_numbers(self, P, s):
        # print(P)  # Used for debugging
        if P.isdigit():  # Does the string evaluate to a number?
            if int(P) > 59:  # Is the number greater than 59
                self.win.bell()
                return False  # Disallow
            return True  # Allow
        elif P=='':
            return True
        else:
            self.win.bell()  # Error sound
            return False


    win.mainloop()
