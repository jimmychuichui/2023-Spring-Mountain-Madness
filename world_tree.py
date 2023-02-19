import minigame

class Node:
    def __init__(self, data):
        self.data = data
        self.optionL = None
        self.optionR = None
        self.previous = None

    def __repr__(self):
        return self.data


node_start = Node("Start")



# create room nodes
node_1 = Node("1")

node_2 = Node("2")

node_3 = Node("3")

node_4 = Node("4")

node_5 = Node("5")

node_6 = Node("6")

node_7 = Node("7")

node_8 = Node("8")

node_9 = Node("9")

node_10 = Node("10")

node_11 = Node("11")

node_12 = Node("12")

node_end = Node("End")


# link the rooms together

node_start.optionL = node_1
node_start.optionR = node_2

node_1.optionL = node_3
node_1.optionR = node_4

node_2.optionL = node_5
node_2.optionR = node_6

node_3.optionR = node_7

node_4.optionL = node_7
node_4.optionR = node_8

node_5.optionL = node_8
node_5.optionR = node_9

node_6.optionL = node_9

node_7.optionR = node_10

node_8.optionL = node_10
node_8.optionR = node_11

node_9.optionL = node_11

node_10.optionR = node_12

node_11.optionL = node_12

node_12.optionL = node_end



node_itr = node_start
dead = False
while not dead and node_itr.data != "End":
    option = input("R/L/B: ").lower()
    temp = node_itr


    if option == 'l':
        if node_itr.optionL == None:
            dead = True
            print("Ded")
        else:
            node_itr = node_itr.optionL
            node_itr.previous = temp
            print(node_itr.data, node_itr.previous)
    elif option == 'r':
        if node_itr.optionR == None:
            dead = True
            print("Ded")
        else:
            node_itr = node_itr.optionR
            node_itr.previous = temp
            print(node_itr.data, node_itr.previous)
    elif option == 'b':
        if node_itr.previous == None:
            print("Cannot go back further")
        else:
            node_itr = node_itr.previous
            print("Current node: " + node_itr.data)

    else:
        print("Correct input not recieved")  

    if node_itr == node_4:
        minigame.run()

    
    

#print("You Won")

