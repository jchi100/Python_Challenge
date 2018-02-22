# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 20:04:03 2018

@author: Jing

Data Science BootCamp Python PyBank
"""

import csv

fileName = os.path.join('..', 'PyBank', 'budget_data_2.csv')
 
dates = []
revenues = []
avechgBtwMonths=[]
 
with open(fileName) as csvDataFile:
    csvReader = csv.reader(csvDataFile,delimiter=',',)
    try:
        next(csvReader)
        for row in csvReader:
            dates.append(row[0])
            revenues.append(int(row[1]))
    except csv.Error as e:
        sys.exit('file %s, line %d: %s' % (fileName, reader.line_num, e))
 
totalMonths = len(dates)

totalRevenue = sum(i for i in revenues)



for row in range(0,totalMonths-1):
    revenue_change = revenues[row]-revenues[row+1]
    avechgBtwMonths.append(revenue_change)
    

sumRevenueChange = sum(j for j in avechgBtwMonths)
averageRevenueChange = sumRevenueChange/totalMonths

maxRevenueChange = max(avechgBtwMonths)
minRevenueChange = min(avechgBtwMonths)

maxindex = avechgBtwMonths.index(maxRevenueChange)
maxRevenueChangeDate = dates[maxindex]

minindex = avechgBtwMonths.index(minRevenueChange)
minRevenueChangeDate = dates[minindex]


print("Total Months: " + str(totalMonths))
print("Total Revenue: " + '${:,.2f}'.format(totalRevenue))
print("Average Revenue Change: " + '${:,.2f}'.format(averageRevenueChange))
print("Greatest Increase in Revenue: "+ maxRevenueChangeDate + " (" +'${:,.2f}'.format(maxRevenueChange) +")")
print("Greatest Increase in Revenue: "+ minRevenueChangeDate + " (" +'${:,.2f}'.format(minRevenueChange) +")")


    


