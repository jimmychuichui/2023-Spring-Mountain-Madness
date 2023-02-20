import os
import sys

def get_path():
    if getattr(sys, 'frozen', False):
        # If the application is run as a PyInstaller executable, use the
        # special sys._MEIPASS attribute to get the path to the temporary
        # directory
        base_path = sys._MEIPASS + "/data"
    else:
        # If the application is run from source code, use the current
        # directory
        base_path = os.path.abspath(".")

    return base_path