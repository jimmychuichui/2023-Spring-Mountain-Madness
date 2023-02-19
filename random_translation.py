import random

def give_tranlation(risk, options, translations_left, translations_right):
    risks = [100, 87.5, 75, 62.5, 50, 37.5, 25, 12.5]
    
    good_translations = []
    bad_translations = []

    if options[0] == 1 and options[1] == 1:
        choice1 = random.randint(0,1)
        if choice1 == 1:
            good_translations = translations_left
            bad_translations = translations_right
        else:
            good_translations = translations_right
            bad_translations = translations_left

    elif options[0] == 1:
        good_translations = translations_left
        bad_translations = translations_right
    elif options[1] == 1:
        good_translations = translations_right
        bad_translations = translations_left
    else:
        print("This is impossible")

    print(good_translations)
    choice2 = random.randrange(0,100)

    if choice2 < risks[risk-1]:
        print(random.choice(good_translations), end=' ')
    else:
        print(random.choice(bad_translations), end= ' ')
    input()

while True:
    give_tranlation(2, [1, 1], ['left'], ['right'])
    input()