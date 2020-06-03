NUM1 = input(                "num1=")
NUM2 = input("                num2=")

NUM11 = float(NUM1)
NUM22 = float(NUM2)

c = input("input + or - or * or /     :")
if c == "+":
    a = NUM11+NUM22
if c == "-":
    a = NUM11-NUM22
if c == "/":
    a = NUM11/NUM22
if c== "*":
    a = NUM11*NUM22
else:
    print("            ")

print(NUM11,c,NUM22,"=",a)
