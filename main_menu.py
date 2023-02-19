from colorama import Fore, Back, Style
import time
import os
import text

CLEAR_SCREEN = ''
if os.name == 'nt':
    CLEAR_SCREEN = 'cls'
else:
    CLEAR_SCREEN = 'clear'

os.system('cls' if os.name == 'nt' else 'clear')

def opening_logo(len):
    os.system(CLEAR_SCREEN)
    colors = [Fore.BLACK, Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.RED]
    for i in range(len):
        i = i%5
        print(rf"""{colors[i]}
 ___        ______    ________  ___________                                                                                 
|"  |      /    " \  /"       )("     _   ")                                                                                
||  |     // ____  \(:   \___/  )__/  \\__/                                                                                 
|:  |    /  /    ) :)\___  \       \\_ /                                                                                    
 \  |___(: (____/ //  __/  \\      |.  |                                                                                    
( \_|:  \\        /  /" \   :)     \:  |                                                                                    
 \_______)\"_____/  (_______/       \__|                                                                                    
  __    _____  ___                                                                                                          
 |" \  (\"   \|"  \                                                                                                         
 ||  | |.\\   \    |                                                                                                        
 |:  | |: \.   \\  |                                                                                                        
 |.  | |.  \    \. |                                                                                                        
 /\  |\|    \    \ |                                                                                                        
(__\_|_)\___|\____\)                                                                                                        
 ___________  _______        __      _____  ___    ________  ___            __  ___________  __      ______    _____  ___   
("     _   ")/"      \      /""\    (\"   \|"  \  /"       )|"  |          /""\("     _   ")|" \    /    " \  (\"   \|"  \  
 )__/  \\__/|:        |    /    \   |.\\   \    |(:   \___/ ||  |         /    \)__/  \\__/ ||  |  // ____  \ |.\\   \    | 
    \\_ /   |_____/   )   /' /\  \  |: \.   \\  | \___  \   |:  |        /' /\  \  \\_ /    |:  | /  /    ) :)|: \.   \\  | 
    |.  |    //      /   //  __'  \ |.  \    \. |  __/  \\   \  |___    //  __'  \ |.  |    |.  |(: (____/ // |.  \    \. | 
    \:  |   |:  __   \  /   /  \\  \|    \    \ | /" \   :) ( \_|:  \  /   /  \\  \\:  |    /\  |\\        /  |    \    \ | 
     \__|   |__|  \___)(___/    \___)\___|\____\)(_______/   \_______)(___/    \___)\__|   (__\_|_)\"_____/    \___|\____\) 
                                                                                                                            

        """)
        time.sleep(0.2)
        os.system(CLEAR_SCREEN)

print(f"{Style.BRIGHT}{Fore.BLUE}Welcome!{Style.RESET_ALL}")
print()
print(f'''{Fore.WHITE}
You are stuck in a mysterious land. It is full of strange creature and even stranger locations
Even the language that the locals speak is unintelligable to you. It is perhaps a French dialect.
Nevertheless, you must attempt to translate the useful tips the locals will give you. 
Unfortuntely, your <GENERIC TRANSLATE APP> is corrupted and does not translate properly. To debug,
you must solve puzzles. {Fore.YELLOW}The accuracy of the resulting translation depends on your puzzle-solving
proficiency.{Fore.WHITE} 

Beware of unscrupulous creatures luring you to certain death. But play it too safe, and you could become forever lost.

Forever lost: In the Strange Land of Translatione

Press Enter to begin
''')
input()









