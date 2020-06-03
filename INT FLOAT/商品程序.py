#RICHARD

n1=input("the price for the first item(RMB):")
print("  ")
n2=input("the price for the second item(RMB):")
print("  ")
n3=input("the price for the third item(RMB):")
print("  ")
n4=input("how many item1 do you buy?")
print("  ")
n5=input("how many item2 do you buy?")
print("  ")
n6=input("how many item3 do you buy?")
input("  ")

n1=float(n1)
n2=float(n2)
n3=float(n3)
n4=float(n4)
n5=float(n5)
n6=float(n6)

print("the cost for item 1 is",n1*n4,"RMB")
print("  ")
print("the cost for item 2 is",n2*n5,"RMB")
print("  ")
print("the cost for item 3 is",n3*n6,"RMB")
input("  ")

N1=n1*n4
N2=n2*n5
N3=n3*n6

TTC=N1+N2+N3
TTC1=str(TTC)

print("the total cost is ",TTC1,"RMB")
print("  ")
print("the tax is 17.5 percent")
input("     ")
print("the total tax is ",(TTC*17.5//100),"RMB")
print("                               ")
print("the total cost after tax is",(TTC*117.5//100),"RMB")
input("                               ")

TTCC=TTC*117.5//100

PAY=input("so you are going to pay(RMB):   ")

PAY=float(PAY)
if PAY<(TTC*17.5//100):
    print("that's not enough.go away!")
    
elif PAY>(TTC*17.5//100):
    CHANGE=PAY-TTCC
    CHANGE=str(CHANGE)
    print("ok.Here's your change:",CHANGE,"RMB")
    print("bye bye.")

else:
    print("Thank you, bye bye.")
