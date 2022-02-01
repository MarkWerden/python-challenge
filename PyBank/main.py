# Important to note, some mechanics of this code was taken from outside sources. In an attempt
# to show that I am understanding it rather than just copy-pasting, I attempted to explain where
# I can. - Mark

import os
import csv

file = "Resources/budget_data.csv"

TotalMonths = 1 # Defined as 1 because it ignores the header row
Total = 0
MonthlyChange = [] # Defined as a list beccause of its appending function 
GreatestIncrease = 0
GreatestDecrease = 0
GMI = 0 # Short for "Greatest Month Increase"
        # its the variable that will hold the associated month when profits are highest
GMD = 0 # Short for "Greatest Month Decrease" 
        # its the variable that will hold the associated month when profits are lowest

with open(file) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    csv_header = next(csvreader)
    row = next(csvreader) # Defines the value "Row" as any value that isn't the header
    PreviousRow = int(row[1]) # Defines the value based off of what the "Row" value is (for finding the average)
    Total = Total + int(row[1]) # Needed because it is likely that the for loop skips the first value

    for row in csvreader:
        TotalMonths = TotalMonths + 1 
        Total = Total + int(row[1])
    
        RevenueChange = int(row[1]) - PreviousRow # Subtracts the value defined by the row and the "PreviousRow" variable
        MonthlyChange.append(RevenueChange) # Adds the value to the associated list
        PreviousRow = int(row[1]) # A means to "reset" the variable for it not to incorrectly calculate the changes
        
        if int(row[1]) > GreatestIncrease: # This "if" statement compares the value of the cell to the value of the variable.
            GreatestIncrease = int(row[1]) # If it is higher than it, it will replace the value with the new one and take
            GMI = row[0]                   # the associated month in that row.
            
        if int(row[1]) < GreatestDecrease: 
            GreatestDecrease = int(row[1]) # The same logic applies to this "if" statement as well
            GMD = row[0]
        
    AverageChange = sum(MonthlyChange)/len(MonthlyChange) # Takes the average of the changes within the list, using the list created by appending.
    
    Maximum = max(MonthlyChange) # These two are essentially the same as using Excel formulas
    Minimum = min(MonthlyChange)
    
    print(f"Financial Analysis")
    print(f"---------------------------")
    print(f"Total Months: {TotalMonths}")
    print(f"Total: ${Total}")
    print(f"Average Change: ${AverageChange:.2f}")  # The "2f" is saying to stop at 2 decimal places.
    print(f"Greatest Increase in Profits:, {GMI}, (${Maximum})")
    print(f"Greatest Decrease in Profits:, {GMD}, (${Minimum})")

output = "Analysis/ExportedBudgetData.txt"

with open(output, 'w') as txtfile:
    txtfile.write(f"Financial Analysis\n")
    txtfile.write(f"---------------------------\n")  # "\n" is essentially telling the script to start it on a new line
    txtfile.write(f"Total Months: {TotalMonths}\n")
    txtfile.write(f"Total: ${Total}\n")
    txtfile.write(f"Average Change: ${AverageChange:.2f}\n")
    txtfile.write(f"Greatest Increase in Profits:, {GMI}, (${Maximum})\n")
    txtfile.write(f"Greatest Decrease in Profits:, {GMD}, (${Minimum})\n")
