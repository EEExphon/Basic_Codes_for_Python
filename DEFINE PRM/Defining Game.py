import random

print("__________")
print("1 | axe  |")
print("--|------|")
print("2 | sword|")
print("--|------|")
print("3 | fist |")
print("----------")
print("\n")


def fight (dice):
    result = 0
    for i in range (dice):
        throw = random.randint(1,6)
        result = result + throw
    return result

def fightm (dice):
    resultm = 0
    for i in range (dice):
        throwm = random.randint(1,6)
        resultm = resultm + throwm
    return resultm


YUI = input("Now,choose one kind of attack . ( 1 / 2 / 3 )")

if YUI == "1":
    resultd = fight (20)
    print("Your SP this time is :",resultd)
    resultf = fightm (10)
    print("Your enemy's SP is :",resultf)
    if resultd > resultf:
        print("YOU WIN")
    if resultd == resultf:
        print("NOBODY WINS")
    if resultd < resultf:
        print("YOU LOSE")
if YUI == "2":
    resultd = fight (20)
    print("Your SP this time is :",resultd)
    resultf = fightm (10)
    print("Your enemy's SP is :",resultf)
    if resultd > resultf:
        print("YOU WIN")
    if resultd == resultf:
        print("NOBODY WINS")
    if resultd < resultf:
        print("YOU LOSE")
if YUI == "3":
    resultd = fight (20)
    print("Your SP this time is :",resultd)
    resultf = fightm (10)
    print("Your enemy's SP is :",resultf)
    if resultd > resultf:
        print("YOU WIN")
    if resultd == resultf:
        print("NOBODY WINS")
    if resultd < resultf:
        print("YOU LOSE")
