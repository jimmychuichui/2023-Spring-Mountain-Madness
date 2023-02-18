# Compile lists

file = open("functions2.txt")
file.readline()

def make_list(file):
    lst = []
    for line in file:
        content = line.strip('\n')
        lst.append(content)
    return lst

#print(make_list(file))
