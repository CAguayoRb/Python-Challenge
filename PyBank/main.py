import csv
import os

budgetdata_csv = os.path.join("python-challenge/PyBank/Resources/budget_data.csv")

with open(budgetdata_csv, newline = "") as data_csv:
    csvreader = csv.reader(data_csv, delimiter=',')
    header = next(csvreader)

    months_var = 0 
    profit_loss_total = []
    total_months = []
    change_months = []

    #get total number of monts, total profit & loss, and data.
    for row in csvreader:
        total_months.append(row[0])
        profit_loss_total.append(int(row[1]))
 

    for i in range(len(profit_loss_total)-1):
        change_months.append(profit_loss_total[i+1]-profit_loss_total[i])
    
    total_months = len(total_months) 
    total_sum = sum(profit_loss_total)
    average_change = round(sum(change_months)/len(change_months), 2)
    greatest_increase = max(change_months)
    greatest_decrease = min(change_months)

    print('Financial Analysis;')
    print('-------------------------------------')
    print(f'Total Months: {total_months}')
    print(f'Total: ${total_sum}')
    print(f'Average Change: ${average_change}')
    print(f'Greatest Increase in Profits: ${greatest_increase}')
    print(f'Greatest Decrease in Profits: ${greatest_decrease}')
   

import sys
sys.stdout = open("python-challenge/PyBank/Analysis/budget_data_analysis.txt", "w")

print("Financial Analysis;")
print("-------------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_sum}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: ${greatest_increase}")
print(f"Greatest Decrease in Profits: ${greatest_decrease}")
   
sys.stdout.close()


