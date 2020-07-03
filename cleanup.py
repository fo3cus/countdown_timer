#!/usr/bin/python3

import tkinter as tk
import pygame


class MainWindow(tk.Frame):
    iMin = 29
    iSec = 59
    rMin = 29
    rSec = 59
    working = 0

    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

    def create_window(self):
        pass


def all_exit():
    root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    root.attributes("-fullscreen", True)
    main = MainWindow(root)
    main.configure(background='black')
    main.config(cursor="none")  # hide the mouse cursor
    root.bind('<x>', all_exit)
    # main.bind('<F1>', gostop)
    # main.bind('<F2>', reset)
    # main.bind('<F3>', alarm)
    # main.bind('<Button-3>', popup)
    main.pack(side="top", fill="both", expand=True)
    root.mainloop()

