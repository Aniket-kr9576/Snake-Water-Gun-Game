import random

computer = random.choice([-1 , 0 , 1])

youstr = input("Enter the choice: ")

youdic = {"s": 1 , "w": -1 , "g": 0}

reversedict = {1:"snake" , -1:"water" , 0:"gun"}

you = youdic[youstr]

print(f"you choose {reversedict[you]}\n computer choose {reversedict[computer]}")

if(computer==you):
    print("its a draw")

else:
    '''
      if(computer==-1 and you==1): (computer - you) = -2
        print("You win !")
    elif(computer==-1 and you==0): (computer - you) = -1
        print("You lose !")
    elif(computer==1 and you==-1): (computer - you) = 2
        print("You lose !")
    elif(computer==1 and you==0):  (computer - you) = 1
        print("You win !")
    elif(computer==0 and you==-1): (computer - you) = 1
        print("You win !")
    elif(computer==0 and you==1):  (computer - you) = -1
        print("You lose !")
    
    The below logic is written on the basis of the value of computer - you
'''
    if((computer-you)==-1 or (computer-you)==2):
        print("You lose !")
    else:
        print("You win !")