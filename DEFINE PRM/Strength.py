import random 
def strength (dice):
    result = 0
    for i in range (dice):
        throw = random.randint(1,6)
        result = result + throw
    print("your strength is",result)
    while result <= 17:
        result = 0
        for i in range (dice):
            throw = random.randint(1,6)
            result = result + throw
        print("your strength is",result)
        
strength(3)