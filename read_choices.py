import os
import text

def read_for_choice(node_number, node_name):
    with open("left_right_choices.txt", "r") as file:
        lines = file.readlines()

    start_index = 0
    end_index = 0
    checkfor = "**Node " + str(node_number)+ ": " + node_name
    for i, line in enumerate(lines):
        #if line.startswith("**") and node_name in line and str(node_number) in line:
        if checkfor in line:
            i+=1
            start_index = i
            while i < len(lines) and not lines[i].startswith("**"):
                #print(lines[i], end="")
                i += 1
            end_index = i
            
    
    return start_index+1, end_index



# print(read_for_choice(9, "T"))
#index = read_for_diaglog(11, "D")
#print(index)
    
