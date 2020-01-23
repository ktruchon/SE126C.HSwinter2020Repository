#PRACTICE 1B - SOLUTION
#REQUIRED: Name, Lab #

#STARTING DOCUMENTATION
#-program prompt
#-pseudocode
#-starting notes (post-analysis)
#-anything else that might help you/someone reviewing your work to understand the program they're about to read/run

#VARIABLE DICTIONARY: a list of variables used and description of the data they intend to hold
#sumtotalTemps          the sum total of all tempFs entered during session
#totalTemps             the total number of temps entered during session

#FUNCTIONS----------------------------------------------------------



#BASE PROGRAM CODE / MAIN()-----------------------------------------

#initialize variables that will change/grow inside of loop
#initialize: to initialize a variable means to store an initial value

sumtotalTemps = 0
totalTemps = 0

print("Welcome to my Fahrenheit to Celsisu Conversion Program!\n\n")

#answer has been edited to hold the # of temps for this program run
answer = int(input("Enter # of temps you wish to convert: "))

while totalTemps < answer:

    tempF = float(input("\nPlease enter the temperature in Fahrenheit: "))

    sumtotalTemps += tempF      
    #same as: --> sumtotalTemps = sumtotalTemps + tempF

    totalTemps += 1

    #convert tempF to Celsius (tempC)
    tempC = (tempF - 32) * (5 / 9)
    
    print("\t\t TOTAL TEMPS: ", totalTemps)
    #format the print statement
    print("\t\t TEMPERATURES: {0:.1f}F | {1:.1f}C".format(tempF, tempC))

    #print("TEMP F: ", tempF, " TEMP C: ", tempC)
    #build a way out
    #answer = input("Would you like to enter another temp? [y/n]: ")


#find average of tempF
avgTempF = sumtotalTemps / totalTemps

avgTempC = (avgTempF - 32) * (5 / 9)

print("\n\n-------------------------------------\n")

print("TOTAL TEMPS: ", totalTemps)
print("AVERAGE TEMPERATURES: {0:.1f}F | {1:.1f}C".format(avgTempF, avgTempC))

print("\n-------------------------------------\n")
print("\n\n\nThank you for using my program. Goodbye!")


