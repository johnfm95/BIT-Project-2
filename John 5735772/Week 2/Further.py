import urllib2
import json

from pprint import pprint
import sys
url = "http://dev.c0l.in:9999/"
response = urllib2.urlopen(url).read()
data = json.loads(response)
raw_input = "type a company ID: "
SectorType = str(data["Sector"])
print "Sector is: " + sector
