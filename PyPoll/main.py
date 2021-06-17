import os
import csv

poll_csv = 'python-challenge/PyPoll/Resources/election_data.csv'

with open(poll_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    totalvotes = 0
    votes = []
    candidates = []
   
    for row in csvreader:
        votes.append(row[0])
        candidates.append(row[2])

    total_votes = (len(votes))

#Get info for each candidate:

#Otooley
otooley_votes = (int(candidates.count("O'Tooley")))
otooley_percentage = (otooley_votes/total_votes) * 100
otooley_final = round(otooley_percentage, 3)

#Correy
correy_votes = (int(candidates.count("Correy")))
correy_percentage = (correy_votes/total_votes) * 100
correy_final = round(correy_percentage, 3)

#Li
li_votes = (int(candidates.count("Li")))
li_percentage = (li_votes/total_votes) * 100
li_final = round(li_percentage, 3)

#Khan
khan_votes = (int(candidates.count("Khan")))
khan_percentage = (khan_votes/total_votes) * 100
khan_final = round(khan_percentage, 3)

#Get the winner:
if otooley_votes > khan_votes > correy_votes > li_votes:
    winner = "O'Tooley"
elif correy_votes > khan_votes > li_votes > otooley_votes:
    winner = "Correy"
elif li_votes > khan_votes > correy_votes > otooley_votes:
    winner = "Li"
elif khan_votes > correy_votes > li_votes > otooley_votes:
    winner = "Khan"


print("Election Results")
print("----------------------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------------------")
print(f"Khan: {khan_percentage}% ({khan_votes})")
print(f"Correy: {correy_percentage}% ({correy_votes})")
print(f"Li: {li_percentage}% ({li_votes})")
print(f"O'Tooley: {otooley_percentage}% ({otooley_votes})")
print("-------------------------------------------")
print(f"Winner: {winner}!")

import sys
sys.stdout = open("python-challenge/PyPoll/Analysis/election_data_analysis.txt", "w")

print("Election Results")
print("----------------------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------------------")
print(f"Khan: {khan_percentage}% ({khan_votes})")
print(f"Correy: {correy_percentage}% ({correy_votes})")
print(f"Li: {li_percentage}% ({li_votes})")
print(f"O'Tooley: {otooley_percentage}% ({otooley_votes})")
print("-------------------------------------------")
print(f"Winner: {winner}!")

sys.stdout.close()