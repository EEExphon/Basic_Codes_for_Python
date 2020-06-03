print("Make a list!")

BB = [ ]
YON="y"
PPO=0
while YON=="y":
    YU=input("Add an element:")
    PPO=PPO+1
    BB.append(YU)
    YON=input("Enter 'y' in order to add a new element.")
input("(press enter to look at the whole list)")
for i in range (0,PPO):
    print(i,"---",BB[i-1])
    
