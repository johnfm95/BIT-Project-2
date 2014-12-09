# -*- coding: cp1252 -*-
#print "Welcome to the Data Processing Tool!"
#x = raw_input("To continue, type 'ENTER': ")
#if x == ("ENTER"):
#    print " "
#else:
#    quit()
#
#Words = ("John", "Sam", "Tom", "Sai", "Samira")
#isinlist = False
#
#while True:
#    x = raw_input ("Username: ")
#    for word in Words:
#        if x == word:
#            isinlist = True
#    if isinlist == True:
#        break
#
#Words = ("Password123", "Password", "P")
#isinlist = False

#while True:
#    x = raw_input ("Password: ")
#    for word in Words:
#        if x == word:
#            isinlist = True
#    if isinlist == True:
#        break
#
#print "Welcome!"

import urllib2
import json
from pprint import pprint
import sys
url = "http://dev.c0l.in:9999/"
response = urllib2.urlopen(url).read()
data = json.loads(response.decode('utf8'))

objectsCount = sys.getsizeof(data)
print objectsCount
userInput = raw_input ("Type company ID: ")

for x in range(5000):
    if int(userInput) == int(data[x]['id']):
        print data[x]['company']['name']
        print data[x]['company']['current_liabilities']
        print data[x]['company']['non_current_liabilities']
        print data[x]['company']['current_assets']
        print data[x]['company']['non_current_assets']
        print data[x]['company']['equity']
        print "£"
        


