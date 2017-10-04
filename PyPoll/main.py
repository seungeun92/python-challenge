#You will be given two sets of poll data (election_data_1.csv and election_data_2.csv). 
#Each dataset is composed of three columns: Voter ID, County, and Candidate. 
#Your task is to create a Python script that analyzes the votes and calculate

import csv

totalvotes = 0
candidatenames = []
votecount = {}

pullfile = 'election_data_2.csv'
pushfile = 'PyPollResults_SL.txt'

with open(pullfile, newline='') as csvfile:
	
	csvreader = csv.reader(csvfile, delimiter = ',')
	
	#skip first line
	next(csvfile)

	for row in csvreader:
		
		#The total number of votes cast
		totalvotes = totalvotes + 1
		#import candidate lists
		candidateall = row[2]

		#A complete list of candidates who received votes
		if candidateall not in candidatenames:
			candidatenames.append(candidateall)
			votecount[candidateall] = 0
		
		#The total number of votes each candidate won - store in dictionary
		votecount[candidateall] = votecount[candidateall] + 1

with open(pushfile, "w") as txt_file:	

	print ("Election Results")
	print ("---------------------------")
	print ("Total Votes: " + str(totalvotes))
	print ("---------------------------")
	
	txt_file.write("Election Results\n")
	txt_file.write("---------------------------\n")
	txt_file.write("Total Votes: " + str(totalvotes)+"\n")
	txt_file.write("---------------------------\n")

	winning_count = 0
	winnername = ""
	
	for candidate in votecount:
		#The percentage of votes each candidate won
		candidate_counts = votecount[candidate]
		candidate_percent = (votecount[candidate]/totalvotes)*100
		print (str(candidate) + ": " + f"{candidate_percent:.1f}%" + " ("+str(candidate_counts)+")")
		txt_file.write(str(candidate) + ": " + f"{candidate_percent:.1f}%" + " ("+str(candidate_counts)+")\n")
		
		#The winner of the election based on popular vote.
		if (candidate_counts > winning_count):
			winning_count = candidate_counts
			winnername = candidate
	
	print ("---------------------------")
	print ("Winner: " + winnername)
	print ("---------------------------")
	txt_file.write("---------------------------\n")
	txt_file.write("Winner: " + winnername+"\n")
	txt_file.write("---------------------------\n")










