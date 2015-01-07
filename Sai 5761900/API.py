
import csv
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
        print "The Company name is:       " + data[x]['company']['name']
        print "Company Sector is:         " + data[x]['sector']
        print "Current Liabilities:      £" + str(data[x]['company']['current_liabilities'])
        print "Non Current Liabilites:   £" + str(data[x]['company']['non_current_liabilities'])
        print "Current Assets:           £" + str(data[x]['company']['current_assets'])
        print "Non Current Liabilities:  £" + str(data[x]['company']['non_current_assets'])
        print "Equity:                   £" + str(data[x]['company']['equity'])


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
        print "The Company name is:       " + data[x]['company']['name']
        print "Company Sector is:         " + data[x]['sector']
        print "Purchases:                £" + str(data[x]['company']['purchases'])
        print "Interest Payables:        £" + str(data[x]['company']['interest_payable'])
        print "Sales:                    £" + str(data[x]['company']['sales'])
        print "Expenses:                 £" + str(data[x]['company']['expenses'])
        print "Interest Recivables:      £" + str(data[x]['company']['interest_receivable'])
        print "Opening Stock:            £" + str(data[x]['company']['opening_stock'])
        print "Closing Stock:            £" + str(data[x]['company']['closing_stock'])

data = open ("API", "rb")
byte = data.read(1)
while byte != "1":
   byte = data.read(1)
   data.close()
   






