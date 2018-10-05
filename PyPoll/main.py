import os
import csv

# Path to csvfile
csvfile = os.path.join("election_data.csv")

# print heading
print("Election Results")
print("----------------------------------")

with open(csvfile, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    # create each candidate as a list to append next
    votes = []
    Khan = []
    Correy = []
    Li = []
    OTooley = []

    #appending rows to each candidate variable
    for row in csvreader:

        votes.append(float(row[0]))

        if row[2] == "Khan":
            Khan.append(row[2])

        if row[2] == "Correy":
            Correy.append(row[2])

        if row[2] == "Li":
            Li.append(row[2])

        if row[2] == "O'Tooley":
            OTooley.append(row[2])

    #Vote counts by candidate
    Kcount = len(Khan)
    Ccount = len(Correy)
    Lcount = len(Li)
    Ocount = len(OTooley)

    #Candidate %s
    Kpercent = round(Kcount/len(votes)*100,3)
    Cpercent = round(Ccount/len(votes)*100,3)
    Lpercent = round(Lcount/len(votes)*100,3)
    Opercent = round(Ocount/len(votes)*100,3)

    #print out total votes and candidate %s and total votes
    print(f"Total Votes: {len(votes)}")
    print("----------------------------------")
    print(f"Khan: {Kpercent}% ({Kcount})")
    print(f"Correy: {Cpercent}% ({Ccount})")
    print(f"Li: {Lpercent}% ({Lcount})")
    print(f"O'Tooley: {Opercent}% ({Ocount})")
    print("----------------------------------")
    
    #determine the overall winner
    winner = ()
    if Kpercent > max(Cpercent, Lpercent, Opercent):
        winner = "Khan"
    if Cpercent > max(Kpercent, Lpercent, Opercent):
        winner = "Coorey"
    if Lpercent > max(Kpercent, Cpercent, Opercent):
        winner = "Li"
    if Opercent > max(Kpercent, Cpercent, Lpercent):
        winner = "O'Tooley"

    print(f"Winner: {winner}")

    print("----------------------------------")

#exported to text file using bash


