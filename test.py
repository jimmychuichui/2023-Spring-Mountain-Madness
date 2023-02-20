import sys
import os

# Get the path to the temporary directory where data files are located
# at runtime
if getattr(sys, 'frozen', False):
    # If the application is run as a PyInstaller executable, use the
    # special sys._MEIPASS attribute to get the path to the temporary
    # directory
    base_path = sys._MEIPASS
else:
    # If the application is run from source code, use the current
    # directory
    base_path = os.path.abspath(".")

# Build the full path to the data file
data_path = os.path.join(base_path, "data.txt")

print(data_path)