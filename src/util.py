# To define functions that will be utililty for this apps.

import os
import sys

from argparse import ArgumentParser

#command option parser
def get_option():
    argparser = ArgumentParser()
    '''
    argparser.add_argument("-t", "--type", type=int,
                            default=False,
                            help="file type.")
    '''
    argparser.add_argument("-v", "--version",
                            default=False,
                            help="Show version info.",
                            action="store_true")

    return argparser.parse_args()
