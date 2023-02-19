import time
from colorama import Fore, Style
import random



i = 0
j = 0
#start_int is the digit where the line starts in the file
#end_int is the digit where the line ends in the file
#delay_scalar is the multiple with which the size of the target sentence is multiplied for a general effect
#attention_const measures delay from one line printing to the next
def print_Narrate(start_int, end_int, delay_scalar, attention_const):
    start_index = start_int-1
    text = open("Dialogue.txt")
    file = text.readlines()
    #reads from Dialogue file
    for i in range((end_int) - (start_index)):
        #Sentence
        print((file[start_index+i].strip('\n')))
        time_of_sentence = len(file[i+(start_index)])/10
        time.sleep(attention_const+(delay_scalar*time_of_sentence))
    print(80*'/') 

#prints inserted text in a Bold and Cyan with an extra space at the end
def print_Cyan(txt):
    print(f"{Style.BRIGHT}{Fore.CYAN}"+txt.strip('\n'),f"{Style.RESET_ALL}", end = "")

#prints out a translation and the % of getting the correct translation from Translations.txt
def print_Outcome(attempts, start_int):
    lst = [100, 87.5, 75, 62.5, 50, 37.5, 25, 12.5]
    percent = lst[attempts-1]
    checker = random.randint(1,100)
    file = open("Translations.txt")
    line = file.readlines()
    if percent>=checker:
        success = 0
    else:
        success = 1
    print("Chance of success {:.2f}".format(percent))
    print(success)
    print(line[start_int+success])

#prints put random garbage
def print_garbage(size):
    file = open("French Words.txt")
    line = file.readlines()
    for i in range(size):
        random_num = random.randint(0,125)
        print_Cyan((line[random_num]))
    print()