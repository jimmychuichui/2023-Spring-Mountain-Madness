import minigame
import world_tree
import nodes



node_itr = nodes.node_start
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

    if node_itr == nodes.node_4:
        minigame.run()

    