import minigame

import nodes

class Node:
    def __init__(self, data):
        self.data = data
        self.optionL = None
        self.optionR = None
        self.previous = None

    def __repr__(self):
        return self.data



# create room nodes
nodes.node_start = Node("Start")

nodes.node_1 = Node("1")

nodes.node_2 = Node("2")


nodes.node_3 = Node("3")


nodes.node_4 = Node("4")


nodes.node_5 = Node("5")


nodes.node_6 = Node("6")


nodes.node_7 = Node("7")


nodes.node_8 = Node("8")


nodes.node_9 = Node("9")


nodes.node_10 = Node("10")


nodes.node_11 = Node("11")


nodes.node_12 = Node("12")


nodes.node_end = Node("End")


# link the rooms together

nodes.node_start.optionL = nodes.node_1
nodes.node_start.optionR = nodes.node_2

nodes.node_1.optionL = nodes.node_3
nodes.node_1.optionR = nodes.node_4

nodes.node_2.optionL = nodes.node_5
nodes.node_2.optionR = nodes.node_6

nodes.node_3.optionR = nodes.node_7

nodes.node_4.optionL = nodes.node_7
nodes.node_4.optionR = nodes.node_8

nodes.node_5.optionL = nodes.node_8
nodes.node_5.optionR = nodes.node_9

nodes.node_6.optionL = nodes.node_9

nodes.node_7.optionR = nodes.node_10

nodes.node_8.optionL = nodes.node_10
nodes.node_8.optionR = nodes.node_11

nodes.node_9.optionL = nodes.node_11

nodes.node_10.optionR = nodes.node_12

nodes.node_11.optionL = nodes.node_12

nodes.node_12.optionL = nodes.node_end


#create_nudes()

def get_options(node):
    pos = node
    options = [1,1]
    if pos.optionL == None:
        options[0] = 0
    if pos.optionR == None:
        options[1] = 0
    #print(options)
    return options

def move(node):
    pos = node
    dead = False
   
    option = input("(1/2): ").lower()
    temp = pos


    if option == '1':
        if pos.optionL == None:
            dead = True
            return "dead"
        else:
            pos = pos.optionL
            pos.previous = temp
            #print('Current room:',pos.data, 'Previous room:',pos.previous)
    elif option == '2':
        if pos.optionR == None:
            dead = True
            return "dead"
        else:
            pos = pos.optionR
            pos.previous = temp
            #print('Current room:',pos.data, 'Previous room:',pos.previous)
    elif option == 'b':
        if pos.previous == None:
            print("Cannot go back further")
        else:
            pos = pos.previous
            #print("Current node: " + pos.data)
    elif option == 'exit':
        return 'dead'
    else:
        print("Correct input not recieved")  
        return move(pos)
    return pos

    ##if pos == nodes.node_4:
        ##minigame.run()

    
    

#print("You Won")

