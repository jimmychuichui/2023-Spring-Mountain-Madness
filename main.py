import minigame
import random_translation
import world_tree
import nodes
import text




pos = nodes.node_start
dead = False
while not dead and pos.data != "End":
    print('\n')
    pos = world_tree.move(pos)
    if pos == 'dead':
        print("You died")
        dead = True
    elif pos != nodes.node_start:
        print("Current room number:",pos.data)
        print("Time for off-brand wordle!")
        score = minigame.run()
        print(score)
        random_translation.give_tranlation(2, [1, 1], ['left'], ['right'])
