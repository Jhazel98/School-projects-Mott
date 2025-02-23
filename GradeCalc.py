# Jazmin Hazel
# PseudoCode program 6
# COMS 170 - WWW01
# 3/17/2022
# This application evaluates classroom data from another file


def Main():
# -------------------------------------------------------------------------------
# Variable Name         Data Type           Purpose
# -------------------------------------------------------------------------------
# strChoice             string              Store user menu option

    strChoice = ""

#start loop
    while strChoice != "X":

#display header
        print("-------------------------------------------------")
        print(" MISS HAZEL'S CLASS GRADES")
        print("-------------------------------------------------")
        print("")

#Display menu options
        print("D: Display Grades")
        print("C: Calculate Class Average")
        print("X: Exit")

#Get user selection
        strChoice = input("Enter your menu selection: ")

#evaluate menu selection
        if strChoice == "C":
            CalcAverage()
        elif strChoice == "D":
            DisplayData()
        elif strChoice == "X":
            print("\n" *3)
            print("Goodbye")
        else:
            print("\n" *3)
            print("ERROR: Menu selection unkown")
        if strChoice != "X":
            print("\n" * 3)
            input("Press enter to continute...")
            print("\n" * 3)
            
def DisplayData():

# -------------------------------------------------------------------------------
# Variable Name         Data Type           Purpose
# -------------------------------------------------------------------------------
# intCount              integer             number lines
# intGrade              integer             Store grades taken from file


    intCount = 0

    try:
            
    #open the file
        infile = open("grades.txt","r")

    #read the first line
        line = infile.readline()
        strLine = infile.readline()
        
    #loop until end of file
        while strLine != "":
            intGrade = int(line)
            intCount += 1
            print(str(intCount) + ": " + strLine.strip())
            strLine = infile.readline()
        infile.close()

    except IOError:
        print("ERROR: File not found.")

    except ValueError:
        print("ERROR: Value error. Data not found or incompatible data type.")

    
def CalcAverage():

# -------------------------------------------------------------------------------
# Variable Name         Data Type           Purpose
# -------------------------------------------------------------------------------
# intCount              integer             counts the number of grades
# intGrade              integer             stores grades from data file
# intTotal              integer             stores the sum of all grades
# fltAverage            float               stores the average of all grades

    intGrade = 0
    intTotal = 0
    intCount = 0

    try:
    
    #open the file
        infile = open("grades.txt","r")
        

    #read the first line
        line = infile.readline()
        strLine = infile.readline()

        while strLine != "":
            intGrade = int(line)
            intTotal += intGrade
            intCount += 1
            strLine = infile.readline()
            
        infile.close()
        
        fltAverage = format(intTotal / intCount, '.2f')

        print("The class average is: " + (fltAverage))

    
    except IOError:
        print("ERROR: File not found.")

    except ValueError:
        print("ERROR: Value error. Data not found or incompatible data type.")



Main()
