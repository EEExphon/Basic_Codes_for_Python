for i in range (1,20):
    print("count number",i)
    input("  ")
print("ok,finishied")
#----------------------------------------------
input("          press enter to start.")
i=input("enter  the  number  of  times  table:")
j=input("enter the highest number to multiply:")
i=int(i)
j=int(j)
for i in range (1,i+1):
    print("          ",i,"times table")
    for j in range (1,j+1):
        print("             ",j,"*",i,"=",i*j)
    input("")
        
