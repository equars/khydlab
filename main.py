########
#   KHYDLAB Hydraulic Simulator for machine
#   author : Imai @equars
#   license : MIT license
#   requirement : normal module for python, numpy
########

import os
import sys

#import numpy as np
import tkinter as tk

import src.util as util

version = "v0.0"

#main
def main():
    #command option parser
    args = util.get_option()
    if args.version :
        print(version)
    else:
        pass

if __name__ == '__main__':
    main()
