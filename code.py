#  GUESS THE NUMBER

import random
target=random.randint(1, 100)
while True:
    userchoice=input("Guess the number or type 'Q' to 'Quit':")
    if(userchoice=="Q"):
        print("---Game ended---")
        break
    
    userchoice=int(userchoice)
    if(userchoice==target):
        print("Success : correct answer")
        break
    elif(userchoice<target):
        print("Number is too small....Guess the bigger number...")
    else:
        print("Number is too big....Guess the smaller number...")
        
    
print("----Game Over----")