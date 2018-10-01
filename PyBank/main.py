import os
import csv

# Path to collect data from the Resources folder
csvfile = os.path.join("budget_data.csv")


print("FINANCIAL ANALYSIS")
print("----------------------------------")


with open(csvfile, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    netTotal = []
    date = []
    change = []

    for row in csvreader:
        netTotal.append(float(row[1]))
        date.append(row[0])

    print(f"Total Months: {len(date)}")
    print(f"Total: ${round(sum(netTotal))}")

    for x in range(1, len(netTotal)):
        change.append(netTotal[x] - netTotal[x-1])
        avg_change = sum(change)/len(change)

        max_change = max(change)
        min_change = min(change)

        #max_change_date = str(date[change.index(max(change))])
        #min_change_date = str(date[change.index(min(change))])

    print(f"Average Change: ${round(avg_change)}")
    print(f"Greatest Increase in Profits: {max_change_date} (${max_change})")
    print(f"Greatest Decrease in Profits: {min_change_date} (${min_change})")
    
  
    

  




