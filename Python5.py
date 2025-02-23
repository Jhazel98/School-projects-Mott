# Jazmin Hazel
# Program 4
# COMS 170 - WWW01
# 1/23/2022
# This application is a random number guessing game

# -------------------------------------------------------------------------------
# Variable Name         Data Type           Purpose
# -------------------------------------------------------------------------------
#strChoice              string              stores user input for menu
# strReturn             string              user presses enter to return to menu
# intVistors            integer             stores number of visitors
# intMinutes            integer             stores number of minutes
# fltSubtotal           float               stores subtotal
# fltServiceFee         float               stores service fee
# fltGrandtotal         float               stores total cost per group


#Display header
print("*************************************************************************")
print("*                     UBER AWESOME ESCAPE ROOM                          *")
print("*************************************************************************")
print(" ")



#Define functions
def DisplayFees(): 
    print(" ")
    print("**********************************")
    print("MENU OF CHOICES")
    print("**********************************")
    print("35 minutes       $85.00")
    print("60 minutes       $130.00")
    print("75 minutes       $155.00")
    print(" ")
    strReturn = (input("To return to menu press enter"))


def CalculateAdmission():
    print(" ")
    print("*" * 25)
    print("ADMISSION CALCULATOR")
    print("*" * 25)
    print(" ")
    intVisitors = int(input("Enter the number of visitors: "))
    intMinutes = int(input("Enter the number of minutes: "))
    if intMinutes == 35:
        fltSubtotal = 85.00
    if intMinutes == 60:
        fltSubtotal = 130.00
    if intMinutes == 75:
        fltSubtotal = 155.00
    print(fltSubtotal)
    fltGrandtotal = (CalcServiceFee(fltSubtotal) + fltSubtotal)
    print("GROUP PRICE ", format(fltGrandtotal, '.2f'))
    print("PER PERSON PRICE ", format(fltGrandtotal / intVisitors , '.2f'))
    print(" ")
    strReturn = (input("To return to menu press enter"))
    
def CalcServiceFee(fltSubtotal):
    fltServiceFee = (fltSubtotal * 0.05)
    return fltServiceFee

#Display menu options
def main():
    #define Variable
    strChoice = ""
    while strChoice != "X":
        print(" ")
        print("C: Calculate admission")
        print("D: Display admission options")
        print("X: Exit the application")
#user inputs menu selection, call corresponding function
        strChoice = input("Enter your menu selection: ")
        if strChoice == "D":
            DisplayFees()   
        if strChoice == "C":
            CalculateAdmission()

main()



   

    


          
