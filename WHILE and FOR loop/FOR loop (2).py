BG=input("which number do you wanna start with?")
HM=input("how many loops do you want?")

HM=int(HM)
BG=int(BG)

for i in range (BG,HM+1):
    print("count number:",i)

print("now the loop has stopped")
print(HM)
#----------------------------------------------------
input("")
#----------------------------------------------------    
RT=input("input a number:")

RT=int(RT)

for i in range (1,13):
    print("numbers:",RT*i)

print("now the loop has stopped")
#----------------------------------------------------
input("")
#----------------------------------------------------
for i in range (1,13):
    print(i,"times table")
    for j in range (1,13):
        print(i*j)
        
