

import urllib2


import json
from pprint import pprint
import sys
url = "http://dev.c0l.in:9999/"
response = urllib2.urlopen(url).read()
data = json.loads(response.decode('utf8'))

count = 0

companyData = ["Financial", "Industrial goods", "services", "healthcare", "basic materials", "technology", "consumer goods", "basic materials", "utilities", ]
UserFind = raw_input("How many companies are under this sector?")
for odd in data:
   if odd["sector"] == UserFind :
       count = count + 1
print count


##count = 0
##
##companyData = ["Financial", "Industrial", "services", "healthcare", "basic materials", "technology", "consumer goods"]
##UserFind = raw_input("How many company data are available?")
##for odd in data:
##   if odd["company"] == UserFind :
##       count = count + 1

##print count






