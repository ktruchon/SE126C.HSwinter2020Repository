#Week 3 Day 1: LISTS DEMO

#LISTS can hold multiple data points and store them to "memory" to be used later in our program

#BASE PROGRAM CODE-------------------------------------------------------------------

import csv

#you should ALWAYS have a total records var for your first few attempts at file reading
total_records = 0

#holds all salaries in file for total print at end
total_salaries = 0


#CREATE EMPTY LISTS -- processor needs to know that they're lists and not variables
#create a list for each field within the file (also err on the side of the longest record)

name = []
age = []
salary = []
extra = []

print("          {0:.10}\t{1:.10}\t   {2:10}".format("NAME", "AGE", "SALARY"))

with open("C:/Users/KTRUCHON/Downloads/example.csv") as csvfile:

    file = csv.reader(csvfile)
 
    for rec in file:
        
        total_records += 1  #SHORTHAND VERSION of: total_records = total_records + 1
 
        #print(rec)

        #STORE FIELD DATA INTO LISTS
        name.append(rec[0])#append (add) value stored in rec[0] into the list 'name'
        age.append(rec[1])
        salary.append(float(rec[2]))#<-- casting salary value as float for easier numeric processing later

        extra.append("x") #can be stored value or constant value

        #print("{0:10}\t{1:10}\t${2:10.2f}".format(rec[0], rec[1], int(rec[2])))

#"CLOSING" FILE ------- disconnecting from file path ---------------------------------
#we can disconnect because all file data is now stored into LISTS

#print the full records from the file
#this will require PROCESSING THE LIST
#"process list" = FOR LOOP

for index in range(2, total_records): #index will start at 0 and run as many times as the value stored in 'records' -- index will grow by +1 each time through the for loop


    #in order to access the individual values within each list, we use 'index'
    #when we appended the lists, we did it record by record, so each record's data, although spread over multiple lists, is all found at the same location (index)
    print("INDEX: ", index, "{0:10}\t{1:10}\t${2:10.2f}".format(name[index], age[index], salary[index]))


#process the lists to calculate total_salaries

for index in range(0, total_records):

    total_salaries += salary[index]


#print final values: total records processed and total salary of all employees in file
print("TOTAL RECORDS: ", total_records)
print("TOTAL SALARY: ${0:.2f}".format(total_salaries))