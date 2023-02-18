#this is for starting the game

import chapter_1
import os.path
import csv
import helper_functions

def main():
    print("Hello traveller, weclome to Paris!")


    #read data.csv file
    #if it is not exisiting, create a new one, let the user to input the data, start the game from the beginning
    #if it is exisiting, read the data, start the game from the last checkpoint
    if os.path.exists("data.csv"):
        #read the data decide which chapter to start
        helper_functions.chapeter_selecter()
        return




    print("What is your name?")

    name = input()
    chapter = 1
    #create and write the name and the chapter to the data.csv file
    with open("data.csv", "w") as file:

        # create a CSV writer object
        writer = csv.writer(file)
        # write the name to the CSV file
        writer.writerow([name])
        writer.writerow([chapter])

    
   

    print("Hello " + name + ", it is a pleasure to meet you!")
    print("Your mission is to find the treasure in the city of Paris.")
    print("You will be given a series of clues to help you find the treasure.")

    print("Please pick an option:")
    print("1. Start the game")
    print("2. Exit the game")
    
    flag = True
    while flag:
        option1 = input()
        if option1 == "1":
            flag = False
            chapter_1.branch1(name)
            
        elif option1 == "2":
            flag = False
        else:
            print("Invalid option, please try again!")












if __name__ == "__main__":
    main()