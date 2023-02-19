import os

def read_for_diaglog(node_number, node_name):
    with open("Dialogue.txt", "r") as file:
        lines = file.readlines()

    start_index = 0
    end_index = 0
    for i, line in enumerate(lines):
        if line.startswith("**") and node_name in line and str(node_number) in line:
            i+=1
            start_index = i
            while i < len(lines) and not lines[i].startswith("**"):
                print(lines[i], end="")
                i += 1
            end_index = i
            
    
    return start_index+1, end_index


#index = read_for_diaglog(6, "Z")
#print(index)
    
