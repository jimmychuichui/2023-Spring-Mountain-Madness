import minigame
import random_translation
import world_tree
import nodes
import text
import read_text





pos = nodes.node_start
dead = False

wordle_choices = []

while not dead and pos.data != "End":
    print('\n')
    pos_copy = pos
    pos = world_tree.move(pos)
    if pos == 'dead':
        #print("You died")
        read_text.read_for_diaglog(int(pos_copy.data), 'D')
        dead = True
    elif pos.data == '12':
        print(wordle_choices)
    elif pos != nodes.node_start:
        read_text.read_for_diaglog(int(pos.data), 'A')

        #print("Current room number:",pos.data)
        read_text.read_for_diaglog(int(pos.data), 'B')
        #print("Time for off-brand wordle!")
        score = minigame.run()
        wordle_choices.append(score[1])
        print(wordle_choices)
        print(score[0])
        options = world_tree.get_options(pos)
        random_translation.give_tranlation(score[0], options, ['left'], ['right'])

