class Animal():
    def __init__ (C,name,code,DOB,species):

        C.code=code
        C.name=name
        C.species=species
        C.DOB=DOB

AnimalList=[]

MORE="Y"
n=0###
while MORE=="Y" or MORE=="y":
    n=n+1###
    N=str(n)###
    Newcode=input("Enter the animal code   :")
    Newname=input("Enter the animal name   :")
    Newspec=input("Enter the animal species:")
    NewDaOB=input("Enter the date of birth :")

    ANIMAL=Animal(Newname,Newcode,NewDaOB,Newspec)
    
    AnimalList.append(ANIMAL)
    
    MORE=input("Add another animal? (Y/N)")
    print("\n")

LEN=len(AnimalList)
for i in range (LEN):
    print("Animal",(i+1))
    print(AnimalList[i].code)
    print(AnimalList[i].name)
    print(AnimalList[i].species)
    print(AnimalList[i].DOB)
    print("\n")
    
print("Enter 'name' to see all the names.")
print("Enter 'code' to see all the codes.")
print("Enter 'DOB' to see all the date of birth.")
print("Enter 'species' to see all the species.")


