import csv
import urllib2
import json

raw_input("Press Enter")

print " "
print "Welcome to the Data Processing Tool"
x = raw_input("To continue, type 'START': ")
if x == ("START"):
    print " "
elif x == ("Start"):
    print " "
elif x == ("start"):
    print " "
else:
    print ("Error, please try again"), quit()

print "(Example Username = 'User', Example Password = 'Pass')"

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
url = "http://dev.c0l.in:9999/"
response = urllib2.urlopen(url).read()
data = json.loads(response)

count = 0
print ("financial", "industrial goods", "services", "healthcare", "basic materials", "technology", "consumer goods", "basic materials", "utilities")
UserFind = raw_input("Type any Sector: ").lower()
for odd in data:
   if odd["sector"] == UserFind :
       count = count + 1
print " "
print "Amount of companies in sector are:", count

print " "
print "Sector filter"
UserInput = raw_input ("Type any sector:       ").lower()
print " "

alist = []
for x in range(5000):
    if str(UserInput) == data[x]['sector']:
        Company = data[x]['company']['name']
        ID = str(data[x]['id'])        
        alist.append("Company = "+Company+"           ID = "+ID)
alist.sort()
for company in alist:
    print company
    
print ""
print "Statement of Financial Position"
UserInput2 = raw_input ("Type any company ID:       ")
print ""

for x in range(5000):
    if int(UserInput2) == int(data[x]['id']):
        CN1 = data[x]['company']['name']
        S1 = data[x]['sector']
        CL = str(data[x]['company']['current_liabilities'])
        NCL = str(data[x]['company']['non_current_liabilities'])
        CA = str(data[x]['company']['current_assets'])
        NCA = str(data[x]['company']['non_current_assets'])
        EQ = str(data[x]['company']['equity'])
        print "The Company name is:       " + CN1
        print "Company Sector is:         " + S1
        print "Current Liabilities:      £" + CL
        print "Non Current Liabilites:   £" + NCL
        print "Current Assets:           £" + CA
        print "Non Current Assets:       £" + NCA
        print "Equity:                   £" + EQ

url = "http://dev.c0l.in:8888/"
response = urllib2.urlopen(url).read()
data = json.loads(response)

count = 0
print " "
print ("2010","2011", "2012", "2013", "2014")
UserYear = int(raw_input("Type any year: "))
for current in data:
   if current["fiscal_year_beginning"] == UserYear:
       count = count + 1
print " "
print "Amount of companies starting in this fiscal year are:", count

print " "
count = 0
print ("financial", "industrial goods", "services", "healthcare", "basic materials", "technology", "consumer goods", "basic materials", "utilities")
UserFind2 = raw_input("Type any Sector: ").lower()
for odd in data:
   if odd["sector"] == UserFind2 :
       count = count + 1
print " "
print "Amount of companies in sector are:", count

print " "
print "Sector filter"
UserInput3 = raw_input ("Type any sector:       ").lower()
print " "

alist2 = []
for x in range(5000):
    if str(UserInput3) == data[x]['sector']:
        Company2 = data[x]['company']['name']
        ID2 = str(data[x]['id'])
        alist2.append("Company = "+Company2+"           ID = "+ID2)
alist2.sort()
for company2 in alist2:
    print company2


print ""
print "Income Statement"
UserInput4 = raw_input ("Type any company ID:       ")
print ""

for x in range(5000):
    if int(UserInput4) == int(data[x]['id']):
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
                      
print " "
opening_stock = input("Enter opening stock:      £")
purchases = input("Enter purchases:          £")
closing_stock = input("Enter closing stock:      £")
sr = input("Enter sales:              £")

result_cos = opening_stock + purchases - closing_stock
cos = result_cos
result_gp = sr - cos
print " "
def cos(opeing_stock, purchases, closing_stock):
    opening_stock
    purchases
    closing_stock
    print "Cost of sales:            £",result_cos

def gp(sr, cos):
    print "Gross profit:             £",result_gp

cos(0, 0, 0)
gp(0, 0)

print " "
print "Saving data in CSV"
with open('Results.csv', 'w') as csvfile:
    fieldnames = ['Company', 'Sector', 'Current Liabilities', 'Non-Current Liabilities', 'Current Assets', 'Non-Current Assests', 'Equity']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader ()
    writer.writerow ({'Company': CN1, 'Sector': S1, 'Current Liabilities': CL, 'Non-Current Liabilities': NCL, 'Current Assets': CA, 'Non-Current Assests': NCA, 'Equity': EQ})
    writer.writerow ({})
    
    fieldnames = ['Company', 'Sector', 'Purchases', 'Interest Payables', 'Sales', 'Expenses', 'Interest Receivables', 'Opening Stock', 'Closing Stock']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader ()
    writer.writerow ({'Company': CN2, 'Sector': S2, 'Purchases': PU, 'Interest Payables': IP, 'Sales': SA, 'Expenses': EX, 'Interest Receivables': IR, 'Opening Stock': OS, 'Closing Stock': CS})
print "......................."
print "Data saved in CSV!"








    
