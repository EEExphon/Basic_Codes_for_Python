PAssword = input("Enter a new password (at least 10 characters):")
LEN = len(PAssword)

while LEN < 10:
    print("Too short! At least 10 characters.")
    PAssword = input("Enter a new password:")
    LEN = len(PAssword)
    
print(PAssword)
