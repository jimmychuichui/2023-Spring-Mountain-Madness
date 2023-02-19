import random
from colorama import Fore, Back, Style

def give_tranlation(risk, options, translation_left, translation_right):
    risks = [95, 90, 82, 75, 62, 50, 35, 15]
    
    good_translation = ''
    bad_translation = ''

    if options[0] == 1 and options[1] == 1:
        choice1 = random.randint(0,1)
        if choice1 == 1:
            good_translation = translation_left
            bad_translation = translation_right
        else:
            good_translation = translation_right
            bad_translation = translation_left

    elif options[0] == 1:
        good_translation = translation_left
        bad_translation = translation_right
    elif options[1] == 1:
        good_translation = translation_right
        bad_translation = translation_left
    else:
        print("This is impossible")

    #print(good_translation)
    choice2 = random.randrange(0,100)

    if choice2 < risks[risk-1]:
        print(good_translation.strip('\n'))
    else:
        print(bad_translation.strip('\n'))

    print()
    print(f"{Fore.YELLOW}{Style.BRIGHT}This tip has a {risks[risk-1]}% chance of being true{Style.RESET_ALL}\n")
    print()


