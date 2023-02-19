import minigame
import world_tree
import nodes



pos = nodes.node_start
dead = False
while not dead and pos.data != "End":
    print('\n')
    pos = world_tree.move(pos)
    
    if pos != nodes.node_start:
        print("Time for off-brand wordle!")
        minigame.run()
