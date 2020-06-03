FCBayern=["诺伊尔","穆勒","聚勒","哈梅斯","莱万多夫斯基","博阿滕","里贝里","罗本","胡梅尔斯","阿拉巴","格纳布里"]
U=len(FCBayern)
fileName = "♂Shang Hai Zoo(array).txt"

with open (fileName,"w") as myFile:
    myFile.write("余世炅最喜欢的拜仁队："+"\n")
    for h in range (U):
        myFile.write(FCBayern[h]+"\n")
