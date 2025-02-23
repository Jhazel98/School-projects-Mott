# Jazmin Hazel
# program 7
# COMS 170 - WWW01
# 4/1/2022
# This application stores multiple pieces of data into one variable

# -------------------------------------------------------------------------------
# Variable Name         Data Type           Purpose
# -------------------------------------------------------------------------------
# fltLapSpeed           float               Store multiple lap speed times                           
# fltNewLap             float               Store user input

#header
print("-" *40)
print("- DOG OLYMPICS RACES")
print("-" *40)

#declare variables
fltLapSpeed = []
fltNewLap = 0

#start loop
while fltNewLap != -1:
    fltNewLap = float(input("Enter lap speed or type -1 to calculate totals: "))
    if fltNewLap != -1:
        fltLapSpeed.append(fltNewLap)

print("\n")

#print fastest, slowest, and average of laps
print("Fastest Lap: " + format(float(max(fltLapSpeed)), '.2f'))
print("Slowest Lap: " + format(float(min(fltLapSpeed)), '.2f'))
print("Average Lap: " + format(float(sum(fltLapSpeed))/(len(fltLapSpeed)), '.2f'))

#header for scores    
print("\nScores" + "\n" + "-" *40 + "\n")

#print all scores entered to screen
for i in range(len(fltLapSpeed)):
    print(str(i+1) + ": " + format(float(fltLapSpeed[i]), '.2f'))




                            
      
