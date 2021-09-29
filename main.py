########
#   KHYDLAB Hydraulic Simulator for machine
#   author : Imai @equars
#   license : MIT license, Copyright (c) 2021 Yosuke Imai
#   requirement : normal module for python, numpy
########

import os
import sys

#import numpy as np
import tkinter as tk

import src.util as util
import src.views as views

version = "v0.0"
locale = "ja_JP"

#main
def main():
    #command option parser
    args = util.get_option()
    locale = args.langue
    util.set_locale(locale)

    if args.version :
        print(version)
    else:
        win = tk.Tk()
        app = views.Wd_main(win)
        app.mainloop()

if __name__ == '__main__':
    main()
