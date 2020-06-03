GENJI = {
    "Name": "Genji",
    "Age": 30,
    "Nationality": "Japan",
    "Ultimate": "Dragon Blade",
    "Skin": "Oni",
    "1": "2"
}

GENJI["Skin"] = "Blackwatch"

for x in GENJI:
    print(x)

input("=======")
    
for i in GENJI:
    print(GENJI[i])
    
input("=======")

for a,b in GENJI.items():
    print(a,b)

PN=input("Enter your player name: ")
GENJI["PlayerName"] = PN
input("=======")
for a,b in GENJI.items():
    print(a,b)

input("=======")

del GENJI["1"]
for a,b in GENJI.items():
    print(a,b)
