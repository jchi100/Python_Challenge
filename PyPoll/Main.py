# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 12:04:31 2018

@author: Jing
"""

import csv
import os

fileName = os.path.join('..', 'PyPoll', 'election_data_2.csv')

 
electionResult = {}
totalVote = 0

with open(fileName) as csvDataFile:
    csvReader = csv.reader(csvDataFile,delimiter=',')
    try:
        next(csvReader)
        for row in csvReader:
            totalVote = totalVote + 1
            #dictionary  electionResult stores candidate name and his/her votes
            if row[2] in electionResult:    #if candidate in the dictionay, vote+1
                vote = electionResult[row[2]]
                electionResult[row[2]]=vote+1
            else:  # insert new candidate name to electionResult dictionay
                electionResult[row[2]]=1
            
    except csv.Error as e:
        sys.exit('file %s, line %d: %s' % (fileName, reader.line_num, e))
        

vote = 0
for candidate in electionResult.items(): 
        if candidate[1]>vote:
            winner=candidate[0]
            vote = candidate[1]
           


with open('ElectionResults.txt','w') as output:
        print("Election Results")   
        output.write("Election Results\n\r")
        print("-----------------------------")
        output.write("-------------------------\n\r")
        print("Total Votes:" + str(totalVote))
        output.write("Total Votes: " + str(totalVote)+"\n\r")
        print("-----------------------------")
        output.write("-------------------------\n\r")
        for item in electionResult.items():
            percent = item[1]/totalVote
            print(item[0] + ":" +'{:.0%}'.format(percent) + "(" + str(item[1])+")")
            output.write(item[0] + ":" + '{:.0%}'.format(percent) + "(" + str(item[1])+")\n\r")
        print("-----------------------------")
        output.write("-------------------------\n\r")
        print("Winner: " + winner)
        output.write("Winner: " + winner +"\n\r")
        print("-----------------------------")
        output.write("-------------------------\n\r")


        
        
