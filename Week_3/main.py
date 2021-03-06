"""
Created on Fri Apr 10 01:19:04 2020

@author: disguy
"""
import time, sys, os

def storyPrint(text, timer):
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(timer)
    print("\n")

def greatestGainAndLoss(inputPath):
    previousRow = None
    currentRow = None
    greatestGain = {"value": 0, "date": ""}
    greatestLoss = {"value": 0, "date": ""}
    totalMonths = 0
    totalProfits = 0
    totalChange = 0
    with open(inputPath, 'r') as f:
        next(f)
        
        for row in f:
            totalMonths += 1
            
            row = row.split(',')
            totalProfits += int(row[1])
            if previousRow is None:
                previousRow = row
                continue
            
            currentRow = row
    
            currentDelta = int(currentRow[1]) - int(previousRow[1])
            
            totalChange += currentDelta
    
            if currentDelta < 0 and currentDelta < greatestLoss["value"]:
                greatestLoss["value"] = currentDelta
                greatestLoss["date"] = currentRow[0]
            elif currentDelta > 0 and currentDelta > greatestGain["value"]:
                greatestGain["value"] = currentDelta
                greatestGain["date"] = currentRow[0]

            previousRow = currentRow
    
    return(greatestLoss, greatestGain, totalMonths, totalProfits, totalChange/(totalMonths - 1))

def printerWriter(grtLoss, grtGain, totalMonths, totalProfits, averageChange, inputPath):
    f = open('Python_Write_File.txt', 'w')

    outputToConsole = f"""
        Financial Analysis
----------------------------------
Total Months:   {totalMonths}
Total:   $ {totalProfits:,}
Average Change:   $ {averageChange:,.2f}
Greatest Increase in Profits: {grtGain['date']} $ {grtGain['value']:,.2f}
Greatest Decrease in Profits: {grtLoss['date']} ($ {grtLoss['value']:,.2f})
"""
    f.write(outputToConsole)
    storyPrint(outputToConsole, .04)

def main():

    try:
        os.remove('./Budget_Data_Totals.txt')
        a = 'Output File already exists. Deleting...'
        storyPrint(a, .04)
    except OSError:
        b = 'Creating File Python_Write_File.txt...'
        storyPrint(b, .04)
        pass
    
    inputPath = os.path.join('Resources', 'budget_data.csv')
    
    grtLoss, grtGain, totalMonths, totalProfits, averageChange = greatestGainAndLoss(inputPath)
    printerWriter(grtLoss, grtGain, totalMonths, totalProfits, averageChange, inputPath)
        
main()



    
    
    