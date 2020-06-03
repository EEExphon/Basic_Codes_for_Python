filename = "Richard's information.txt"

with open (filename) as mf:
    newlist = mf.readlines()

for i in newlist:
    i = i.strip()
    print(i)
