import random

computer = random.choice([-1,0,1])
youInput = input("Enter your choice :")
youDict = {"s":1, "w":-1, "g":0}
reverseDict = {1:"snake", -1:"water", 0:"gun"}
you = youDict[youInput]
print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if computer==you:
    print("Its a Draw")
else:
    if(computer==1 and you==-1):
        print("Computer Win")
    elif(computer==1 and you==0):
        print("You Win")
    elif(computer==-1 and you==1):
        print("You Win")
    elif(computer==-1 and you==0):
        print("Computer Win")
    elif(computer==0 and you==1):
        print("Computer Win")
    elif(computer==0 and you==-1):
        print("You Win")
    