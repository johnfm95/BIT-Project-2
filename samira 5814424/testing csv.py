import csv

import urllib2
import json

url = "http://dev.c0l.in:8888/"
response = urllib2.urlopen(url).read()
data = json.loads(response)

print ""

count = 0
print ("2010","2011", "2012", "2013", "2014")
UserYear = int(raw_input("Type any year: "))
for current in data:
   if current["fiscal_year_beginning"] == UserYear:
       count = count + 1

print "Amount of companies starting in this fiscal year are:  "
print count

url = "http://dev.c0l.in:8888/"
response = urllib2.urlopen(url).read()
data = json.loads(response.decode('utf8'))

user = raw_input("List of Companies beginning in this fiscal year :")
print ""

for x in range(5000):
    if int(user) == int(data[x]['fiscal_year_beginning']):
        xs = data[x]['company'] ['name']

        s = str(data[x] ['sector'])
        print "The company name :  ",xs,"           sector: ",s


#test for absolute path
print "Saving data to CSV file..."
with open('/tmp/pro2.csv', 'wb') as csvfile:
    testwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    headers = ["Company Name", "Sector"]
    
    for json_obj in data:
        company_name = json_obj["company"]["name"]
        sector = json_obj["sector"]
        testwriter.writerow([company_name, sector])
    

print "Done saving file!"
