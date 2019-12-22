#********************************************************************##********************************************************************#
#   PyPoll: main.py
#********************************************************************##********************************************************************#

#********************************************************************#
#   import modules
#********************************************************************#
import os
import csv

#********************************************************************#
#   set a path for the csv file
#********************************************************************#
#   CSV absolute file path:       ('/Users/shanergy/Desktop/SMU_DS/02-Homework/03-Python/Instructions/PyPoll/Resources/election_data.csv')
#   CSV relative file path:       ('..', '..', 'SMU_DS', '02-Homework', '03-Python', 'Instructions', 'PyPoll', 'Resources', 'election_data.csv')
#   main.py absolute file path:   ('/Users/shanergy/Desktop/SMU_DS_Homework/python-challenge/PyPoll/main.py')
#   main.py relative file path:   ('..', '..', 'Desktop', 'SMU_DS_Homework', 'python-challenge', 'PyPoll', 'main.py')

#csvpath Absolute file path:
#csvpath = os.path.join('/Users/shanergy/Desktop/SMU_DS/02-Homework/03-Python/Instructions/PyPoll/Resources/election_data.csv')
#csvpath Relative file path:
csvpath = os.path.join('Desktop', 'SMU_DS', '02-Homework', '03-Python', 'Instructions', 'PyPoll', 'Resources', 'election_data.csv')

#********************************************************************#
#   set variables
#********************************************************************#
totalVotes = 0
winningVoteCount = 0
candidateList = []
rawCandidateList = []
candidateSummaryList = []

#********************************************************************#
#   open CSV file
#********************************************************************#
with open(csvpath, newline='', encoding='utf-8') as csvfile:
   csvreader = csv.reader(csvfile, delimiter=',')
#********************************************************************#
#   pull out header row from csvreader 
#********************************************************************#
   csv_header = next(csvfile)

#********************************************************************#
#   loop through rows of data in CSV file
#********************************************************************#
   for data in csvreader:
       totalVotes += 1
       rawCandidateList.append(data[2])

#********************************************************************#
#   create a distinct list of candidates by name
#********************************************************************#
candidateList = list(set(rawCandidateList))

#********************************************************************#
#   loop through candidate list get candidate, vote counts and voter percentages, then creating candidateSummaryList to use in output
#********************************************************************#
for candidateIndex in range(len(candidateList)):
    candidate = candidateList[candidateIndex]
    candidateVotes = rawCandidateList.count(candidateList[candidateIndex])
    candidatePercentage = float(candidateVotes / totalVotes)
    candidateSummaryList.append([candidate, candidateVotes, candidatePercentage])

    if candidateVotes > winningVoteCount:
        winningVoteCount = candidateVotes
        winningCandidate = candidate

#********************************************************************#
#   sort candidateSummaryList in descending order
#********************************************************************#
candidateSummaryList = sorted(candidateSummaryList, key=lambda x: x[1], reverse= True)

#********************************************************************#
#   print results in terminal
#********************************************************************#
print("Election Results")
print("-------------------------")
print(f"Total Votes: {totalVotes:,}")
print("-------------------------")
for summaryIndex in range(len(candidateSummaryList)):
    print(f"{candidateSummaryList[summaryIndex][0]}: {candidateSummaryList[summaryIndex][2]:.3%} ({candidateSummaryList[summaryIndex][1]:,})")
print("-------------------------")
print(f"Winner: {winningCandidate}")
print("-------------------------")



#********************************************************************#
#   print results to text file
#********************************************************************#
with open("/Users/shanergy/Desktop/SMU_DS_Homework/python-challenge/PyPoll/election_data.txt", "w") as txtfile:
    # txtfile.write("testing, 1, 2, 3, testing...")
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {totalVotes:,}\n")
    txtfile.write("-------------------------\n")
    for summaryIndex in range(len(candidateSummaryList)):
        txtfile.write(f"{candidateSummaryList[summaryIndex][0]}: {candidateSummaryList[summaryIndex][2]:.3%} ({candidateSummaryList[summaryIndex][1]:,})\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winningCandidate}\n")
    txtfile.write("-------------------------\n")
#********************************************************************##********************************************************************#
#   PyPoll: main.py (end)
#********************************************************************##********************************************************************#
