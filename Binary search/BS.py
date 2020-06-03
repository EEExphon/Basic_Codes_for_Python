# ===Definition===

def binsearch (searchlist,searchitem):
    
    start = 0
    stop = len(searchlist) - 1    
    
    while start <= stop:
        
        mid = (stop + start)/2
        mid = int(mid)
        
        if searchitem == searchlist[mid]:
            return True
        
        if searchitem < searchlist[mid]:
            stop = mid - 1
        else:
            start = mid + 1
            
    return False


# ===Main program===

YN = "y"

while YN == "Y" or YN == "y": 

    NumberList = ["1","2","3","4","5","6","7","8","9","0"]

    print("Enter a number:")
    Userinput = input("-- ") 

    if binsearch (NumberList,Userinput):
        print("Nice.")
    else:
        print("Not in the list.")

    print("Do you wanna continue (y/n)?")
    YN = input("-- ")

    print("\n")

print("THX")
