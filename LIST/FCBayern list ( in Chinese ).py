FCBayern=["诺伊尔","穆勒","聚勒","哈梅斯","莱万多夫斯基","博阿滕","里贝里","罗本","胡梅尔斯","阿拉巴","格纳布里"]

M=len(FCBayern)

YU="y"

while YU=="y" or YU=="Y":
    Num=int(input("Give me a number from 0 to 10 to show you a footballer in FCBayern."))
        
    while not Num<=10 and Num>=0:
        Num=int(input("Give me a number from 0 to 10 to show you a footballer in FCBayern."))

    print("The footballer is",FCBayern[Num],".")

    CH=input("Input H to see the whole list,if you don't want, press enter.")
    if CH=="H" or CH=="h":
        for F in range (0,M):
            print(F,FCBayern[F])

    YU=input("Continue? y or n?")
    
print("GOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOD!")
    
