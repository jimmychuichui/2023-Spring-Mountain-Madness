import os
import text



# read from
# Left: until Right:
# then Right: until **

#return an array of strings
# [left, right]

def read_for_choice(node_number, node_name):
    with open("left_right_choices.txt", "r", errors="ignore") as file:
        lines = file.readlines()

    start_index = 0
    end_index = 0
    checkfor = "**Node " + str(node_number)+ ": " + node_name
    arr = ["", ""]
    for i, line in enumerate(lines):
        #if line.startswith("**") and node_name in line and str(node_number) in line:
        if checkfor in line:
            i+=1
            start_index = i
            while i < len(lines) and not lines[i].startswith("**"):

                ##decide if left or right

                if "Left: " in lines[i]:
                    ##add to left
                    arr[0] = lines[i].split("Left: ")[1]
                    i += 1
                    ##loop until right before Right
                    while i < len(lines) and not lines[i].startswith("**"):
                        if "Right: " in lines[i]:
                            break
                        arr[0] = arr[0] + " " + lines[i].strip("\n")
                        i+=1
                        


                if "Right: " in lines[i]:
                    ##add to right
                    arr[1] = lines[i].split("Right: ")[1]
                    i += 1
                    ##loop until right before "**" or end of file
                    while i < len(lines) and not lines[i].startswith("**"):
                        arr[1] = arr[1] + " " + lines[i]
                        i+=1
                
                i += 1
            end_index = i
            
    #text.print_Narrate(start_index+1, end_index, 0.1, 0)
    return arr



#arr = read_for_choice(11, "T")
#print(arr[0])
#print(arr[1])

#print(index)
    
