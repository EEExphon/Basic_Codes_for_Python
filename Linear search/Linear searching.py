def linear (searchlist,searchitem):
    for item in searchlist:
        if item == searchitem:
            return True
    return False

name = ["Tony","Bruce","Richard","Luis"]
n = input("Enter a name:")

found = linear (name, n)

if found == False:
    print(n,"is not in the list.")
else:
    print(n,"is in the list.")
