#this is for starting the game

import chapter_1

def main():
    print("Hello traveller, weclome to Paris!")
    print("What is your name?")

    name = input()

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
            chapter_1.branch1()
            
        elif option1 == "2":
            flag = False
        else:
            print("Invalid option, please try again!")












if __name__ == "__main__":
    main()