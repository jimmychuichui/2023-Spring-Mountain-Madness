import time
from colorama import Fore, Style
import random
import os
import sys
import path_getter


i = 0
j = 0
#start_int is the digit where the line starts in the file
#end_int is the digit where the line ends in the file
#delay_scalar is the multiple with which the size of the target sentence is multiplied for a general effect
#attention_const measures delay from one line printing to the next
def print_Narrate(start_int, end_int, delay_scalar, attention_const):
    start_index = start_int-1

    #get the path dynamiclly 
    data_path = os.path.join(path_getter.get_path(), ".Dialogue.txt")
    #print(data_path)
    text = open(data_path)
    file = text.readlines()
    #reads from Dialogue file
    for i in range((end_int) - (start_index)):
        #Sentence
        print((file[start_index+i].strip('\n')))
        time_of_sentence = len(file[i+(start_index)])/10
        time.sleep(attention_const+(delay_scalar*time_of_sentence))
    print(100*'=') 
    text.close()

#prints inserted text in a Bold and Cyan with an extra space at the end
def print_Cyan(txt):
    print(f"{Style.BRIGHT}{Fore.CYAN}"+txt.strip('\n')+f"{Style.RESET_ALL}", end = "")

#prints out a translation and the % of getting the correct translation from Translations.txt

#prints put random garbage
def print_garbage(size):
    #get the path dynamiclly
    data_path = os.path.join(path_getter.get_path(), ".French Words.txt")
    
    file = open(data_path)
    line = file.readlines()
    print("NPC:  ", end='')
    print(f"{Fore.CYAN}{Style.BRIGHT}\"", end='')
    for i in range(size):
        random_num = random.randint(0,125)
        print_Cyan((line[random_num]))
        if i == size-1:
            print("", end='')
        else:
            print(" ", end ='')
        if i%10 == 0 and i != 0:
            print()
    print(f"{Fore.CYAN}{Style.BRIGHT}\"{Style.RESET_ALL}", end='')
    print()
    print(100*'=') 
    file.close()
