import os

def read_for_diaglog(node_number, node_name):
    with open("Dialogue.txt", "r") as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        if line.startswith("**") and node_name in line and str(node_number) in line:
            i+=1
            while i < len(lines) and not lines[i].startswith("**"):
                print(lines[i], end="")
                i += 1

read_for_diaglog(5, "Z")


    
