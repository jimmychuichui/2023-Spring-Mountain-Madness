import minigame
import time
import random_translation
import world_tree
import nodes
import text
import read_dialogue
import random
import minigame_ultimate





pos = nodes.node_start
'''
if pos.data == '12':
    #print(wordle_choices)
    read_dialogue.read_for_diaglog(int(pos.data), 'A')
    time.sleep(1)
    read_dialogue.read_for_diaglog(int(pos.data), 'B')
    time.sleep(1)
    read_dialogue.read_for_diaglog(int(pos.data), 'C')
    time.sleep(1)
    read_dialogue.read_for_diaglog(int(pos.data), 'E')
    wordle_choices = ['CHECK','BRAIN','HELLO','AUDIO']
    minigame_ultimate.run_ultimate(wordle_choices)
read_dialogue.read_for_diaglog(0, 'A')
'''
dead = False

wordle_choices = []

while not dead and pos.data != "End":
    print('\n')
    pos_copy = pos
    pos = world_tree.move(pos)
    if pos == 'dead':
        #print("You died")
        read_dialogue.read_for_diaglog(int(pos_copy.data), 'D')
        dead = True


    elif pos.data == '12':
        #print(wordle_choices)
        read_dialogue.read_for_diaglog(int(pos.data), 'A')
        time.sleep(1)
        read_dialogue.read_for_diaglog(int(pos.data), 'B')
        time.sleep(1)
        read_dialogue.read_for_diaglog(int(pos.data), 'C')
        time.sleep(1)
        read_dialogue.read_for_diaglog(int(pos.data), '')

        minigame_ultimate.run_ultimate(wordle_choices)

    elif pos != nodes.node_start:
        # Read the room introduction
        read_dialogue.read_for_diaglog(int(pos.data), 'A')
        time.sleep(1)
        text.print_garbage(random.randint(15, 30))
        #print("Current room number:",pos.data)
        # Read beginning of wordle info, run wordle
        read_dialogue.read_for_diaglog(int(pos.data), 'B')
        time.sleep(2)
        if pos == nodes.node_1 or pos == nodes.node_2:
            minigame.instructions()
        score = minigame.run()
        wordle_choices.append(score[1])
        #print(wordle_choices)
        #print(score[0])

        # give the random translations
        # here I will call the read_choices function 
        options = world_tree.get_options(pos)
        random_translation.give_tranlation(score[0], options, ['left'], ['right'])
    

        


