# To define functions that will be utililty for this apps.

import os
import sys

from argparse import ArgumentParser
import gettext

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

    argparser.add_argument("-l", "--langue",
                            default="ja_JP",
                            help="Set language.")

    return argparser.parse_args()

def set_locale(locale):
    path_to_locale_dir = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "../language"
        )
    )

    translater = gettext.translation(
        locale,                   # domain: file name
        localedir=path_to_locale_dir, # dir to lang file
        languages=[locale],          # language
        fallback=False                 # out raw text if .mo not found
    )

    # set _ func
    translater.install()
