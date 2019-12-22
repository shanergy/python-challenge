#********************************************************************##********************************************************************#
#   PyBank: main.py
#********************************************************************##********************************************************************#

#********************************************************************#
#   import modules
#********************************************************************#
import os
import csv

#********************************************************************#
#   set a path for the csv file
#********************************************************************#
#   CSV absolute file path:       ('/Users/shanergy/Desktop/SMU_DS/02-Homework/03-Python/Instructions/PyBank/Resources/budget_data.csv')
#   CSV relative file path:       ('..', '..', 'SMU_DS', '02-Homework', '03-Python', 'Instructions', 'PyBank', 'Resources', 'budget_data.csv')
#   main.py absolute file path:   ('/Users/shanergy/Desktop/SMU_DS_Homework/python-challenge/PyBank/main.py')
#   main.py relative file path:   ('..', '..', 'Desktop', 'SMU_DS_Homework', 'python-challenge', 'PyBank', 'main.py')

#csvpath Absolute file path:
#csvpath = os.path.join('/Users/shanergy/Desktop/SMU_DS/02-Homework/03-Python/Instructions/PyBank/Resources/budget_data.csv')
#csvpath Relative file path:
csvpath = os.path.join('Desktop', 'SMU_DS', '02-Homework', '03-Python', 'Instructions', 'PyBank', 'Resources', 'budget_data.csv')

#********************************************************************#
#   set variables
#********************************************************************#
count = 0
netPandLTotal = 0
previousValue = 0
currentValue = 0
currentChange = 0
greatestIncrease = 0
greatestDecrease = 0
firstMonth = ""
firstMonthValue = 0

#********************************************************************#
#   open CSV file
#********************************************************************#
with open(csvpath, newline='') as csvfile:
   csvreader = csv.reader(csvfile, delimiter=',')
#********************************************************************#
#   pull out header row from csvreader 
#********************************************************************#
   csv_header = next(csvfile)

#********************************************************************#
#   loop through profit and lost data to get values for calculations and output
#********************************************************************#
   for data in csvreader:
    #    print(data)
    #    count = count + 1
       count += 1
       netPandLTotal += float(data[1])
       previousValue = currentValue
       currentValue = float(data[1])
       currentChange = currentValue - previousValue

       if currentChange > greatestIncrease:
           greatestIncrease = currentChange
           greatestIncreaseMonth = str(data[0])

       if currentChange < greatestDecrease:
           greatestDecrease = currentChange
           greatestDecreaseMonth = str(data[0])

       if firstMonth == "":
           firstMonth = str(data[0])
           firstMonthValue = currentValue

avgChange = round(((currentValue - firstMonthValue) / (count - 1)), 2)

#********************************************************************#
#   print results in terminal
#********************************************************************#
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {count}")
print(f"Total: ${int(netPandLTotal):,}")
print(f"Average  Change: ${avgChange:,}")
print(f"Greatest Increase in Profits: {greatestIncreaseMonth} (${int(greatestIncrease):,})")
print(f"Greatest Decrease in Profits: {greatestDecreaseMonth} (${int(greatestDecrease):,})")

#********************************************************************#
#   print results to text file
#********************************************************************#
with open("/Users/shanergy/Desktop/SMU_DS_Homework/python-challenge/PyBank/budget_data.txt", "w") as txtfile:
    # txtfile.write("testing, 1, 2, 3, testing...")
    txtfile.write("Financial Analysis\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Total Months: {count}\n")
    txtfile.write(f"Total: ${int(netPandLTotal):,}\n")
    txtfile.write(f"Average  Change: ${avgChange:,}\n")
    txtfile.write(f"Greatest Increase in Profits: {greatestIncreaseMonth} (${int(greatestIncrease):,})\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatestDecreaseMonth} (${int(greatestDecrease):,})\n")
#********************************************************************##********************************************************************#
#   PyBank: main.py (end)
#********************************************************************##********************************************************************#