# We all have played snake, water gun game in our childhood if you haven't, google the rules of this game and write a python
# program capabale of playing this game with the user

'''
1 for snake 
-1 for water
0 for gun

'''

import random

computer = random.choice([-1 , 0 , 1])

youstr = input("Enter the choice: ")

youdic = {"s": 1 , "w": -1 , "g": 0}

reversedict = {1:"snake" , -1:"water" , 0:"gun"}

you = youdic[youstr]

# By now we have 2 numbers (variables), you and computer

print(f"you choose {reversedict[you]}\n computer choose {reversedict[computer]}")

if(computer==you):
    print("its a draw")

else:
    if(computer==-1 and you==1):
        print("You win !")
    elif(computer==-1 and you==0):
        print("You lose !")
    elif(computer==1 and you==-1):
        print("You lose !")
    elif(computer==1 and you==0):
        print("You win !")
    elif(computer==0 and you==-1):
        print("You win !")
    elif(computer==0 and you==1):
        print("You lose !")
    
    else:
        print("Something went wrong !")