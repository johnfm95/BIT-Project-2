print "Welcome to the Data Processing Tool!"
x = raw_input("To continue, type 'ENTER': ")
if x == ("ENTER"):
    print " "
else:
    quit()

Words = ("John", "Sam", "Tom", "Sai", "Samira")
isinlist = False

while True:
    x = raw_input ("Username: ")
    for word in Words:
        if x == word:
            isinlist = True
    if isinlist == True:
        break

Words = ("Password123", "Password", "P")
isinlist = False

while True:
    x = raw_input ("Password: ")
    for word in Words:
        if x == word:
            isinlist = True
    if isinlist == True:
        break

print "Welcome!"

