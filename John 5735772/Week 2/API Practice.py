UserInput = raw_input("Type a Company ID Number: ")

import urllib
import json

url = "http://dev.c0l.in:9999/"
response = urllib.urlopen(url+UserInput).read()
data = json.loads(response)

Name = str(data["company"]["name"])
Sector = str(data["sector"])
CurrentLiabilities = float(data["company"]["current_liabilities"])
CurrentAssets = float(data["company"]["current_assets"])
NonCurrentAssets = float(data["compnay"]["non_current_assets"])
Equity = float(data["company"]["equity"])

print "Company Name: " + Name
print "Specific Sector: " + Sector
print "Current Liabilities: "+str(CurrentLiabilities)
print "Current Assets: "+str(CurrentAssets)
print "Non-Current Assets: "+str(NonCurrentAssets)
print "Equity: "+str(Equity)
