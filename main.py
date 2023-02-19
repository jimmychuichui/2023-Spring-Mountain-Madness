import time
import os
import random
from colorama import Fore, Back, Style

import minigame
import minigame_ultimate

import world_tree
import nodes

import text
import read_dialogue
import read_choices
import random_translation

CLEAR_SCREEN = ''
if os.name == 'nt':
    CLEAR_SCREEN = 'cls'
else:
    CLEAR_SCREEN = 'clear'

os.system('cls' if os.name == 'nt' else 'clear')



pos = nodes.node_start
read_dialogue.read_for_diaglog(0, 'A')

dead = False

wordle_choices = []

while not dead:
    print('\n')
    pos_copy = pos
    pos = world_tree.move(pos)
    os.system(CLEAR_SCREEN)
    if pos == 'dead':
        #print("You died")
        read_dialogue.read_for_diaglog(int(pos_copy.data), 'D')
        dead = True
        print('\n\n\n')
        for i in range(3):
            print(f'{Fore.WHITE}{Back.RED}GAME OVER{Style.RESET_ALL}')


    elif pos.data == '12':
        read_dialogue.read_for_diaglog(int(pos.data), 'A')
        time.sleep(1)
        read_dialogue.read_for_diaglog(int(pos.data), 'B')
        time.sleep(1)
        read_dialogue.read_for_diaglog(int(pos.data), 'C')
        time.sleep(1)
        read_dialogue.read_for_diaglog(int(pos.data), 'E')
        #wordle_choices = ['CHECK','BRAIN','HELLO','AUDIO']
        minigame_ultimate.instructions()
        os.system(CLEAR_SCREEN)
        score = minigame_ultimate.run_ultimate(wordle_choices)
        if score == 12:
            read_dialogue.read_for_diaglog(int(pos.data), 'D')
        else:
            os.system(CLEAR_SCREEN)
            read_dialogue.read_for_diaglog(int(pos.data), 'W')
            input("Press Enter to end the game:")
            dead = True



    elif pos != nodes.node_start:
        # Read the room introduction
        read_dialogue.read_for_diaglog(int(pos.data), 'A')
        time.sleep(1)
        text.print_garbage(random.randint(15, 30))
        #print("Current room number:",pos.data)
        # Read beginning of wordle info, run wordle
        read_dialogue.read_for_diaglog(int(pos.data), 'B')
        time.sleep(3)
        if pos == nodes.node_1 or pos == nodes.node_2:
            minigame.instructions()
        else:
            input("Press Enter to begin:")
        score = minigame.run()
        wordle_choices.append(score[1])
        #print(wordle_choices)
        #print(score[0])

        # give the random translations
        # here I will call the read_choices function 
        options = world_tree.get_options(pos)
        translations = read_choices.read_for_choice(int(pos.data), "T")
        random_translation.give_tranlation(score[0], options, translations[0], translations[1])

        # Show movement options
        read_dialogue.read_for_diaglog(int(pos.data), 'Z')

    

        


