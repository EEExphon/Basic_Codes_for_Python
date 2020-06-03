import random

def die ():
    number = random.randint(1,6)
    print(number)

yn = "y"

while yn == "y" or yn == "Y":    
    for i in range (0,2):
        print("die",i+1,"===============================================")
        for g in range (0,3):
            print("No.",g+1,"------------------------------")
            die ()
        print("\n")
    yn = input("Continue? y/n")
        
