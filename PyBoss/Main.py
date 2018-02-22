# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 12:49:01 2018

@author: Jing
"""

import csv
import os
from datetime import datetime

fileName = os.path.join('..', 'PyBoss', 'employee_data2.csv')
 
employee={}
#info = []
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'
}
 
with open(fileName) as csvDataFile:
    csvReader = csv.reader(csvDataFile,delimiter=',',)
    try:
        next(csvReader)
        for row in csvReader:
            firstName,lastName = row[1].split(" ")
            dobDate = (datetime.strptime(row[2], '%Y-%m-%d')).date()
            a,b,c =row[3].split("-")
            SSN ="***-**-"+c         
      #      info.extend((firstName,lastName,dobDate,SSN,us_state_abbrev[row[4]]))
         #   employee(row[0]).append(info)
 
            employee.setdefault(row[0], []).append(firstName)
            employee.setdefault(row[0], []).append(lastName)
            employee.setdefault(row[0], []).append(dobDate.strftime('%m/%d/%Y'))
            employee.setdefault(row[0], []).append(SSN)
            employee.setdefault(row[0], []).append(us_state_abbrev[row[4]])
           # del info[:]
    except csv.Error as e:
        sys.exit('file %s, line %d: %s' % (fileName, reader.line_num, e))

with open('employee_data_new.csv','w') as output:
      output.write("Emp ID,First Name,Last Name,DOB,SSN,State\n")
      for key,item in employee.items():
          output.write(key)
          for i in item:
              output.write(","+i)
          output.write("\n")

   