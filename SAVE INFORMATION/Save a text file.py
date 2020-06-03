# write to a text file

fileName = "Example.txt"

with open (fileName,"w") as myFile:
    myFile.write("Bruce (Yang Chen)."+"\n")
    myFile.write("He is so handsome!"+"\n")
    myFile.write("He likes drinking water."+"\n")
    myFile.write("The glass bottle is always with him.")
