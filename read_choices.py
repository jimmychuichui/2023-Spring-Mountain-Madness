import os
import text



# read from
# Left: until Right:
# then Right: until **

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
                lines[i]
                
                i += 1
            end_index = i
            
    text.print_Narrate(start_index+1, end_index, 0.1, 0, "left_right_choices.txt")
    return start_index+1, end_index



print(read_for_choice(3, "T"))

#print(index)
    
