# Some of the code used is based off of what I learned from the Bank assignment and outside sources.
# Like before, I will attempt to explain where I can. Some things I did not explain here are most
# likely explained in the other assignment or was something I learned in class. - Mark

import os
import csv

file = "Resources/election_data.csv"

Total = 0
Votes_Khan = 0
Votes_Correy = 0   # Each represenative has to have their own counter for it to count their own votes.
Votes_Li = 0
Votes_oTooley = 0

with open(file) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)
    
    for row in csvreader:
        Total = Total + 1
    
        if (row[2] == "Khan"):
            Votes_Khan = Votes_Khan + 1    # This "if/else" statement checks to see if the name column
        elif (row[2] == "Correy"):         # has their name in that row. If so, it adds it to the list.
            Votes_Correy = Votes_Correy + 1  
        elif (row[2] == "Li"):
            Votes_Li = Votes_Li + 1
        else:
            Votes_oTooley = Votes_oTooley + 1
            
    Percent_Khan = Votes_Khan / Total      # Pretty self-explanatory, its finding the representative's
    Percent_Correy = Votes_Correy / Total  # votes compared to the total in decimal form.
    Percent_Li = Votes_Li / Total
    Percent_oTooley = Votes_oTooley / Total
    
    ElectionWinner = max(Votes_Khan, Votes_Correy, Votes_Li, Votes_oTooley)
    
    if ElectionWinner == Votes_Khan:
        Winner = "Khan"
    elif ElectionWinner == Votes_Correy: # This "if/else" statement determines who is the winner
        Winner = "Correy"                # based off of the max value collected by the variable.
    elif ElectionWinner == Votes_Li:
        Winner = "Li"
    else:
        Winner = "O'Tooley"

print(f"Election Results")
print(f"---------------------------")
print(f"Total Votes: {Total}")
print(f"---------------------------")
print(f"Khan: {Percent_Khan:.3%} ({Votes_Khan})") # The ".3%" is telling it to stop at 3 decimal places.
print(f"Correy: {Percent_Correy:.3%} ({Votes_Correy})")
print(f"Li: {Percent_Li:.3%} ({Votes_Li})")
print(f"O'Tooley: {Percent_oTooley:.3%} ({Votes_oTooley})")
print(f"---------------------------")
print(f"Winner: {Winner}")
print(f"---------------------------")

output = "Analysis/ExportedElectionData.txt"

with open(output, 'w') as txtfile:
    txtfile.write(f"Election Results\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Votes: {Total}\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Khan: {Percent_Khan:.3%} ({Votes_Khan})\n")
    txtfile.write(f"Correy: {Percent_Correy:.3%} ({Votes_Correy})\n")
    txtfile.write(f"Li: {Percent_Li:.3%} ({Votes_Li})\n")
    txtfile.write(f"O'Tooley: {Percent_oTooley:.3%} ({Votes_oTooley})\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Winner: {Winner}\n")
    txtfile.write(f"---------------------------\n")