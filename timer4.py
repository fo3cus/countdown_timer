from tkinter import font, ttk
import tkinter as tk
import pygame
import configparser
import os
import sys


# * Constant reference to this file's root directory
SETTINGS_FILE = os.path.join(sys.path[0], "settings.ini")

# * Primary instance class
class Timer(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        # * Configure the display window
        self.parent.attributes("-fullscreen", True)
        self.parent.configure(background="black")

        # * Read the settings file into memory
        self.config = configparser.ConfigParser()
        self.config.read(SETTINGS_FILE)

        # * Apply the settings from file
        self.iMin = int(self.config["SETTINGS"]["minutes"])
        self.iSec = int(self.config["SETTINGS"]["seconds"])
        self.iTotal = str(f"{self.iMin:02}") + ":" + str(f"{self.iSec:02}")  # Format loaded numbers with leading zeroes
        self.wMin = self.iMin
        self.wSec = self.iSec
        self.working = 0

        # * Configure the font
        self.fnt = font.Font(family="Helvetica", size=300, weight="bold")
        self.txt = tk.StringVar()
        self.lbl = ttk.Label(root, textvariable=self.txt, font=self.fnt, foreground="white", background="black")
        self.txt.set(self.iTotal)
        self.lbl.place(relx=0.5, rely=0.5, anchor="center")

        # * Bind hotkeys to actions
        self.parent.bind("<x>", self.quit_all)
        self.parent.bind("<F1>", self.go_stop)
        self.parent.bind("<F2>", self.reset)
        self.parent.bind("<F3>", self.alarm)
        self.parent.bind("<Button-3>", self.popup)

        # * Configure the popup menu
        self.menu_pop = tk.Menu(self.parent)
        self.menu = tk.Menu(self.menu_pop, tearoff=0)
        self.menu.config(bg="black", fg="white", relief="raised")
        self.menu.add_command(label="Start/Stop", accelerator="F1", command=self.go_stop, font="Helvetica 16 bold")
        self.menu.add_command(label="Reset", accelerator="F2", command=self.reset, font="Helvetica 16 bold")
        self.menu.add_separator()
        self.menu.add_command(label="Settings", command=self.settings, font="Helvetica 16 bold")
        self.menu.add_separator()
        self.menu.add_command(label="Exit", accelerator="X", command=self.quit_all, font="Helvetica 16 bold")
        self.menu_pop.add_cascade(label="File", menu=self.menu)

        # * Initialise the alarm sound
        pygame.mixer.pre_init(44100, -16, 2, 2048)
        pygame.mixer.init()
        pygame.mixer.music.set_volume(10.0)
        self.alert = pygame.mixer.Sound("assets/alert.wav")

    # * Start and stop the counter
    def go_stop(self, *args):
        if self.working == 1:
            self.working = 0
        else:
            self.working = 1
            self.parent.after(500, self.run_timer)

    # * Reset counter display
    def reset(self, *args):
        if self.working == 1 and self.wMin == 0 and self.wSec == 0:
            self.working = 0
        if self.working == 0:
            self.wMin = self.iMin
            self.wSec = self.iSec
            self.txt.set(self.iTotal)

    # * Exit the program
    def quit_all(self, *args):
        self.parent.destroy()

    # * Performs the countdown
    def run_timer(self):
        if self.working == 1:
            if self.wMin == 0 and self.wSec == 0:
                self.txt.set("00:00")
                self.flash()
                self.alarm()
            else:
                self.txt.set("%02d:%02d" % (self.wMin, self.wSec))
                if self.wSec == 0:
                    self.wMin -= 1
                    self.wSec = 59
                else:
                    self.wSec -= 1
                self.parent.after(1000, self.run_timer)
        else:
            return

    # * Play the alarm
    def alarm(self):
        self.alert.play()

    # * Flash the displayed numbers
    def flash(self):
        if self.working == 1:
            current_colour = str(self.lbl.cget("foreground"))
            if current_colour == "white":
                next_colour = "grey"
            else:
                next_colour = "white"
            self.lbl.configure(foreground=next_colour)
            self.parent.after(1000, self.flash)
        else:
            self.lbl.configure(foreground="white")
            return

    # * Display the popup menu
    def popup(self, event):
        self.menu.tk_popup(event.x_root, event.y_root)

    # * Display settings window
    def settings(self):
        self.working = 0
        self.win = tk.Toplevel()
        Settings(self.win)
        self.win.mainloop()


# * Settings display class
class Settings(tk.Toplevel):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.config = configparser.ConfigParser()
        self.config.read(SETTINGS_FILE)
        self.parent.title("Settings")
        self.parent.config(bg="black", bd="1", relief="flat")
        self.parent.resizable(height=False, width=False)
        self.my_font1 = font.Font(family="Helvetica", size=16, weight="normal")
        self.my_font2 = font.Font(family="Helvetica", size=20, weight="bold")
        self.cfg = configparser.ConfigParser()
        self.cfg.read(SETTINGS_FILE)
        self.minute_value = tk.StringVar(self.parent)
        self.minute_value.set(self.cfg["SETTINGS"]["minutes"])
        self.second_value = tk.StringVar(self.parent)
        self.second_value.set(self.cfg["SETTINGS"]["seconds"])
        self.spinput = self.parent.register(self.validate_numbers)
        self.spin_minutes = tk.Spinbox(
            self.parent,
            validate="key",
            validatecommand=(self.spinput, "%P", "%s"),
            from_=0,
            to=59,
            textvariable=self.minute_value,
            bg="black",
            relief="flat",
            fg="white",
            bd=1,
            width=3,
            font=self.my_font2,
            justify="center",
        )
        self.spin_minutes.grid(row=0, column=0, padx=10, pady=10)
        self.spin_seconds = tk.Spinbox(
            self.parent,
            validate="key",
            validatecommand=(self.spinput, "%P", "%s"),
            from_=0,
            to=59,
            textvariable=self.second_value,
            bg="black",
            relief="flat",
            fg="white",
            bd=1,
            width=3,
            font=self.my_font2,
            justify="center",
        )
        self.spin_seconds.grid(row=0, column=1, padx=10, pady=10)
        self.parent.save_button = tk.Button(
            self.parent,
            text="Save",
            command=self.save,
            font=self.my_font1,
            bg="black",
            relief="flat",
            fg="white",
            bd=1,
            width=5,
            justify="center",
            padx=5,
            pady=5,
        )
        self.parent.save_button.grid(row=1, column=0, padx=10, pady=10)
        self.parent.close_button = tk.Button(
            self.parent,
            text="Close",
            command=self.close,
            font=self.my_font1,
            bg="black",
            relief="flat",
            fg="white",
            bd=1,
            width=5,
            justify="center",
            padx=5,
            pady=5,
        )
        self.parent.close_button.grid(row=1, column=1, padx=10, pady=10)

    # * Commit settings to file
    def save(self):
        if self.spin_minutes.get() == "":
            self.iMin = 0
        else:
            self.iMin = int(self.spin_minutes.get())

        if self.spin_seconds.get() == "":
            self.iSec = 0
        else:
            self.iSec = int(self.spin_seconds.get())
        self.config_file = open(SETTINGS_FILE, "w")
        self.cfg.set("SETTINGS", "minutes", str(self.iMin))
        self.cfg.set("SETTINGS", "seconds", str(self.iSec))
        self.cfg.write(self.config_file)
        self.config_file.close()
        self.iTotal = str(f"{self.iMin:02}") + ":" + str(f"{self.iSec:02}")
        self.close()
        Timer(root).reset()

    # * Close settings window
    def close(self):
        self.parent.destroy()

    # * Validate manual input
    def validate_numbers(self, P, s):
        if P.isdigit():
            if int(P) > 59:
                self.parent.bell()
                return False
            return True
        elif P == "":
            return True
        else:
            self.parent.bell()
            return False


if __name__ == "__main__":
    root = tk.Tk()
    Timer(root).pack()
    root.mainloop()
