COST=input("please tell me your cost(RMB)  :  ")
COSTE=float(COST)
TTC=COSTE*115/100
TTCE=str(TTC)
print("so yoou need to pay me",TTCE,"RMB")
PAY=input("so,you are going to pay(RMB)   :  ")
PAYE=float(PAY)
CHANGE=PAYE-TTCE
CHANGEE=float(CHANGE)
print("here is your change,",CHANGEE,"RMB")
