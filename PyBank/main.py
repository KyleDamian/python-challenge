import os
import csv

# Path to csvfile
csvfile = os.path.join("Resources", "budget_data.csv")

# print heading
print("FINANCIAL ANALYSIS")
print("----------------------------------")


with open(csvfile, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    total = []
    date = []
    change = []

    # create lists for each column in csv file total and date
    for row in csvreader:
        total.append(float(row[1]))
        date.append(row[0])

    # print first two lines of data
    print(f"Total Months: {len(date)}")
    print(f"Total: ${round(sum(total))}")

    # find average change and max and min change
    for x in range(1, len(total)):
        change.append(total[x] - total[x-1])
        avg_change = sum(change)/len(change)

        max_change = max(change)
        min_change = min(change)

        max_change_date = str(date[change.index(max(change))])
        min_change_date = str(date[change.index(min(change))])

    # print the last three lines of data
    print(f"Average Change: ${round(avg_change)}")
    print(f"Greatest Increase in Profits: {max_change_date} (${max_change})")
    print(f"Greatest Decrease in Profits: {min_change_date} (${min_change})")
    
    #exported results to text file using bash
  
    

  




