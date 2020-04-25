# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 03:26:55 2020

@author: disguy
"""
import time, sys, os


def storyPrint(text, timer):
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(timer)
    print("\n")


def votesCounter(inputPath):
    totalVotes = 0
    totalVotesKhan = 0
    totalVotesCorrey = 0
    totalVotesLi = 0
    totalVotesTooley = 0
    winner = ''
    # counter = 0
    with open(inputPath, 'r') as f:
        next(f)
        
        for row in f:
            
            
            totalVotes += 1
            row = row.rstrip('\n').split(",")
            
            if row[2] == 'Khan':
                totalVotesKhan += 1
            elif str(row[2]) == 'Correy':
                totalVotesCorrey += 1
            elif str(row[2]) == 'Li':
                totalVotesLi += 1
            elif str(row[2]) == "O'Tooley":
                totalVotesTooley += 1
            else:
                continue
        if totalVotesKhan > totalVotesCorrey and totalVotesKhan > totalVotesLi and totalVotesKhan > totalVotesTooley:
            winner = 'Khan'
            
        elif totalVotesCorrey > totalVotesKhan and totalVotesCorrey > totalVotesLi and totalVotesCorrey > totalVotesTooley:
            winner = 'Correy'
        elif totalVotesLi > totalVotesKhan and totalVotesLi > totalVotesCorrey and totalVotesLi > totalVotesTooley: 
            winner = "Li" 
        else:
            winner = "O'Tooley"
    
    
    return(totalVotes, totalVotesKhan, totalVotesCorrey, totalVotesLi, totalVotesTooley, winner)

def printerWriter(totalVotes, totalVotesKhan, totalVotesCorrey, totalVotesLi, totalVotesTooley, winner, inputPath):
    f = open('election_data_.txt', 'w')

    
    pKhan = totalVotesKhan / totalVotes
    pCorrey =  totalVotesCorrey / totalVotes
    pLi = totalVotesLi / totalVotes
    pTool = totalVotesTooley / totalVotes
    
    outputToConsole = f"""
       Election Results
----------------------------------
Total Votes:   {totalVotes:,}
----------------------------------
Khan: {pKhan:.3f}%  {totalVotesKhan:,}
Correy: {pCorrey:.3f}%  {totalVotesCorrey:,}
Li: {pLi:.3f}%  {totalVotesLi:,}
O'Tooley': {pTool:.3f}%  {totalVotesTooley:,}
----------------------------------
        Winner: {winner}
----------------------------------
"""

    f.write(outputToConsole)
    storyPrint(outputToConsole, .075)
    f.close()
def main():
    inputPath = os.path.join('Resources', 'election_data.csv')

    totalVotes, totalVotesKhan, totalVotesCorrey, totalVotesLi, totalVotesTooley, winner = votesCounter(inputPath)
    printerWriter(totalVotes, totalVotesKhan, totalVotesCorrey, totalVotesLi, totalVotesTooley, winner, inputPath)
    try:
        os.remove( './Python_Write_File.txt')
        a = 'Output File already exists. Deleting...'
        storyPrint(a, .075)
    except OSError:
        b = 'Creating File Python_Write_File.txt...'
        storyPrint(b, .075)
        pass
    
        
main()












        