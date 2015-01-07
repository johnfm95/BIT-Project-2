raw_input("Press enter")
print " "

print "Welcome to the Data Processing Tool"
x = raw_input("To continue, type 'START': ")
if x == ("START"):
    print " "
else:
    quit()

print "(Example username = 'User', Example Password = 'Pass')"

Words = ("John", "Sam", "Tom", "Sai", "Samira", "User", "U")
isinlist = False

while True:
    x = raw_input ("Username: ")
    for word in Words:
        if x == word:
            isinlist = True
    if isinlist == True:
        break

Words = ("Password123", "Password", "Pass", "P")
isinlist = False

while True:
    x = raw_input ("Password: ")
    for word in Words:
        if x == word:
            isinlist = True
    if isinlist == True:
        break

print "Welcome!"
print " "

import urllib2
import json

url = "http://dev.c0l.in:9999/"
response = urllib2.urlopen(url).read()
data = json.loads(response)

count = 0
print ("financial", "industrial goods", "services", "healthcare", "basic materials", "technology", "consumer goods", "basic materials", "utilities")
UserFind = raw_input("Type any Sector: ")
for odd in data:
   if odd["sector"] == UserFind :
       count = count + 1
print "Amount of companies in sector are: "
print count

print ""
print "Statement of Financial Position"
userInput = raw_input ("Type any company ID:       ")
print ""



for x in range(5000):
    if int(userInput) == int(data[x]['id']):
        CN1 = data[x]['company']['name']
        S1 = data[x]['sector']
        CL = str(data[x]['company']['current_liabilities'])
        NCL = str(data[x]['company']['non_current_liabilities'])
        CA = str(data[x]['company']['current_assets'])
        NCA = str(data[x]['company']['non_current_assets'])
        E = str(data[x]['company']['equity'])
        print "The Company name is:       " + CN1
        print "Company Sector is:         " + S1
        print "Current Liabilities:      £" + CL
        print "Non Current Liabilites:   £" + NCL
        print "Current Assets:           £" + CA
        print "Non Current Assets:       £" + NCA
        print "Equity:                   £" + E


import urllib2
import json

url = "http://dev.c0l.in:8888/"
response = urllib2.urlopen(url).read()
data = json.loads(response)

print " "
count = 0
print ("financial", "industrial goods", "services", "healthcare", "basic materials", "technology", "consumer goods", "basic materials", "utilities")
UserFind = raw_input("Type any Sector: ")
for odd in data:
   if odd["sector"] == UserFind :
       count = count + 1
print "Amount of companies in sector are: "
print count

print ""
print "Income Statement"
userInput = raw_input ("Type any company ID:       ")
print ""

for x in range(5000):
    if int(userInput) == int(data[x]['id']):
        CN2 = data[x]['company']['name']
        S2 = data[x]['sector']
        PU = str(data[x]['company']['purchases'])
        IP = str(data[x]['company']['interest_payable'])
        SA = str(data[x]['company']['sales'])
        EX = str(data[x]['company']['expenses'])
        IR = str(data[x]['company']['interest_receivable'])
        OS = str(data[x]['company']['opening_stock'])
        CS = str(data[x]['company']['closing_stock'])
        print "The Company name is:       " + CN2
        print "Company Sector is:         " + S2
        print "Purchases:                £" + PU
        print "Interest Payables:        £" + IP
        print "Sales:                    £" + SA
        print "Expenses:                 £" + EX
        print "Interest Recivables:      £" + IR
        print "Opening Stock:            £" + OS
        print "Closing Stock:            £" + CS
