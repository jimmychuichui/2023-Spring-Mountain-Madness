import time
import re
import compilelist as compl
import colorama
from colorama import Fore, Back, Style


file = open("listsum.py", 'r')
file_methods = open('functions2.txt')
methods = compl.make_list(file_methods)

file_keywords = open('keywords.txt')
keywords = compl.make_list(file_keywords)


#Initialize colorama


colorama.init(autoreset=True)



def search(word):
    for method in methods:
        search = '\A^('+method+')[(]'
        #print(search)
        method_search = re.search(search, word)
        #print(re.search(search, word))
        if method_search:
            original = method_search.group(1)
            color = 'purple'
            return [original, color] 

##        else:
##            search = method + ''
##            method_search2 = re.search(search, word)
##            if method_search2:
##                original = method
##                color = 'purple'
##                return [original, color]
                
            
        
    for keyword in keywords:
        search = '\A^('+keyword+')'
        #print(search)
        keyword_search = re.search(search, word)
        #print(re.search(search, word))
        if keyword_search:
            original = keyword_search.group(1)
            color = 'orange'
            return [original, color]    

    
    for i in range(len(word)):
        if word[i] == "'":

            print(yo)
            x=i

            string = ""
            found = False

            while not found:
                for char in range(x, len(word)):
                    string = string+char

                    if char == "'":
                        found = True
            
            print(string)
            color = 'green'


            
            
        
        
    color = None
    return [word, color]






def functionSearch(words):
    for i in range(len(words)):
        if words[i] == 'def':
            x = i
            found = False
            while not found:
                if words[x+1] == ' ':
                    x += 1

                    pass

                elif words[x+1] != ' ':
                    original = words[x+1]
                    found = True
    
            original = words[x+1]
            function_name = ''
            for char in original:
                if char !='(':
                    function_name = function_name + char

                else:
                    break

            color = 'blue'
            return [function_name, color, original]
                            
    color = None
    return ['hi', color]




for line in file:
    
    content = line.strip('\n')
    words = content.split(' ')

    for word in words:
        if word == '#':
            i = words.index('#')
            comment = words[i:]
            for x in comment:
                print((Fore.RED + x), end = ' ', flush=True)
            break

          
        else:

            result = search(word)

            if word == 'def':
                result_fun = functionSearch(words)
                word = Fore.YELLOW + word + ' ' + Fore.BLUE + result_fun[0] + Fore.RESET + result_fun[2][len(result_fun[0]):]
                print(word, end=' ', flush=True)
                break
            
            elif result[1] == 'purple':
                
                word = Fore.MAGENTA + result[0] + Fore.RESET + word[len(result[0]):]
                

            elif result[1] == 'orange':
                word = Fore.YELLOW + result[0] + Fore.RESET + word[len(result[0]):]

            


      
        print(word, end=' ', flush=True)
    

    print('')

input('\n.....')




file.close()


