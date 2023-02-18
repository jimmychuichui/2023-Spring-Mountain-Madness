import time

i = 0
j = 0
#start_int is the digit where the line starts in the file
#end_int is the digit where the line ends in the file
#delay_scalar is the multiple with which the size of the target sentence is multiplied for a general effect
#attention_const measures delay from one line printing to the next
def Narrate(start_int, end_int, delay_scalar, attention_const):
    start_index = start_int-1
    text = open('Dialogue.txt')
    file = text.readlines()
    #reads from Dialogue file
    for i in range((end_int) - (start_index)):
        #Sentence
        print((file[start_index+i].strip('\n')))
        time_of_sentence = len(file[i+(start_index)])/10
        time.sleep(attention_const+(delay_scalar*time_of_sentence))
    print(62*'/')