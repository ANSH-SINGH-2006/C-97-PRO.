import random

number=random.randint(1, 9)
chance=int(5)
print("Number Guessing Game!!")
print("Guess a number (between 1-9): ")



while chance>0:
    x=int(input("Enter your guess: "))
    if(x>number):
        chance=chance-1
        print("Your guess is too high, guess a number lesser than "+str(x))
        print("Chances Left: "+str(chance))
        
        
    elif(x<number):
        chance=chance-1
        print("Your guess is too low, guess a number greater than "+str(x))
        print("Chances Left: "+str(chance))
        
        
    else:
        print("You Won!!!")
        break
        
         
else:
        print("You Lost!!!")
