python3 -m PyInstaller main.spec
python3.11 -m PyInstaller --onefile --add-data ".French Words.txt:./data" --add-data ".Dialogue.txt:./data" --add-data ".left_right_choices.txt:./data" --icon= main.py