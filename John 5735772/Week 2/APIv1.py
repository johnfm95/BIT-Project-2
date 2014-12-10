print "Welcome to the Data Processing Tool!"
x = raw_input("To continue, type 'ENTER': ")
if x == ("ENTER"):
    print " "
else:
    quit()

print "(Example username = 'User', Example Password = 'Pass')"

Words = ("John", "Sam", "Tom", "Sai", "Samira", "User")
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

import urllib2
import json

url = "http://dev.c0l.in:9999/"
response = urllib2.urlopen(url).read()
data = json.loads(response)

print ""
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
        
        


