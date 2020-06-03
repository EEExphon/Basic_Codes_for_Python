print("Enter the three sides of a triangle ♂♂♂♂♂♂♂♂♂♂♂♂♂ ")

R=input("enter 'start' to start")

while R != "end":
    
    c=input("This is a hypoteneuse.C=")
    a=input("                      A=")
    b=input("                      B=")

    a=float(a)
    b=float(b)
    c=float(c)

    if (c*c)==(a*a)+(b*b):
        print("This is a right triangle.")
    if (c*c)>(a*a)+(b*b):
        print("This is a obtuse triangle.")
    if (c*c)<(a*a)+(b*b):
        print("This is a acute triangle.")

    print("Do you wanna do that again? ♂♂♂♂♂♂♂♂♂♂♂♂♂")
    R=input("If you wanna end, enter 'end'.")
    
print("THX for using!")
