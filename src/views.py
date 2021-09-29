#define gui window properties

import os
import sys

#import numpy as np
import tkinter as tk

class Wd_big(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.pack()

        w_width = master.winfo_screenwidth()
        w_height = master.winfo_screenheight()
        master.geometry(str(w_width) + "x" + str(w_height))
        master.title("KHYDLAB")
        master.iconbitmap("./imgs/favicon.ico")
        master.config(bg="black")

class Wd_main(Wd_big):
    pass
