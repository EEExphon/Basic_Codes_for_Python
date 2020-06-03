filename="Free text.txt"

LIST=[]

YN="Y"

while YN=="y" or YN=="Y":
    
    New=input(" Write something in your text for this line.")
    LIST.append(New)

    YN=input("continue y/n")

with open (filename,"w") as file:

    for item in LIST:
        file.write(item + "\n")
        
#在for loop 里面用list的时候，只需要在in后面把list的名字输入进去就可以了。

# for item in LIST:
#   print(item)
#   可以这样

#   原本是这样的
# LEN=len(LIST)
# for item in range (LEN):
#   print(LIST[item])
