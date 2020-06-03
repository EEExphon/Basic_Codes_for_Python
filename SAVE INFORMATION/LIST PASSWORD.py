filename = "Usernames.txt"

with open (filename,"w") as mf:
    
    NL = ["BRUCE","RICHARD","LUIS","TONY"]
    PL = ["bruce","richard","luis","tony"]
    yn = "y"
    while yn == "y" or yn =="Y":
        N = input("YOUR NAME : ")
        if N in NL:
            P = input(" PASSWORD : ")

            x = 0
            while NL[x] != N:
                x = x + 1
    
            while P != PL[x]:
                print("Wrong!!!")
                P = input(" PASSWORD : ")
        
            print("Welcome,",NL[x],"!")
        else:
            print("This username is not in our username list.")
            
