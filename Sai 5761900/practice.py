import urllib2
import json
from pprint import pprint
import sys
url = "http://dev.c0l.in:8888/"
response = urllib2.urlopen(url).read()
data = json.loads(response.decode('utf8'))

objectsCount = sys.getsizeof(data)
print objectsCount
userInput = raw_input ("Type company ID: ")

for x in range(500):
    if int(userInput) == int(data[x]['id']):
        print data[x]['company']['name']

