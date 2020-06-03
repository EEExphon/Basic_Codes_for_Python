take = input("Enter something: ")
bbb = input("Which letter do you want to take? ")
bef = input("Befor which letter? ")
LEN = len(take)

counter = 0

for i in range (LEN):
    if take[i] == bbb and take[i+1]:
        counter += 1
    if take[i] == bef:
        break #This break will only break one loop that it is inside.
        
print("There are",counter,"'"+bbb+"'s before the first '"+bef+"' in the string.")
