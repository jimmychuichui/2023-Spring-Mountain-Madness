import time
import turtle as t
import re


# to open a python file and print out the code

file = open("listsum.py", 'r')

turt = t.Turtle()
s = t.Screen()
s.setup(width=500, height=500, startx=0, starty=0)

x = -220
y= 220

size = 8

turt.ht()
turt.penup()
turt.goto(x, y)



for line in file:
    turt.color('black')
    content = line.strip('\n')

    y -= size+size*.2  
    turt.goto(x, y)

    for i in range(0,len(content)):
        turt.write(content[i], move=True, align='left', font=('Menlo', size, 'normal'))
        #print(content[x], end='', flush=True)
        
input('\n.....')

file.close()


