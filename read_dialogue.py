import os
import text
import sys
import path_getter





def read_for_diaglog(node_number, node_name):


    # Build the full path to the data file
    data_path = os.path.join(path_getter.get_path(), ".Dialogue.txt")
    

    with open(data_path, "r") as file:
        lines = file.readlines()
    #print(data_path)

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
            
    
    #return start_index+1, end_index
    #print(start_index+1, " ", end_index)
    text.print_Narrate(start_index+1, end_index, 0.3, 0.2)

    file.close()



#index = read_for_diaglog(11, "A")
#print(index)
    
