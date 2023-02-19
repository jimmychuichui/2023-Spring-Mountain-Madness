import random

def give_tranlation(risk, options, translation_left, translation_right):
    risks = [100, 87.5, 75, 62.5, 50, 37.5, 25, 12.5]
    
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
        print(good_translation)
    else:
        print(bad_translation)
    print()
    print("This tip has a {}% chance of being true".format(risks[risk-1]))


