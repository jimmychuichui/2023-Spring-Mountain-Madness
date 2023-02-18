import os.path
import csv
import chapter_1
def chapeter_selecter():
    # This function will select the chapter to be read
    # It will read the data.csv file and select the chapter
    # It will then call the function from the chapter file
    with open("data.csv", "r") as file:
                reader = csv.reader(file)
                 #sore the name row of data
                name = next(reader)
                # convert the row to a string
                name = str(name[0])


                # read the second row of data
                row = next(reader)
                # convert the row to an integer
                row = int(row[0])
                # if the row is 1, call the branch1 function
                if row == 1:
                    chapter_1.branch1(name)
