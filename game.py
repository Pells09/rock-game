import random
import sys

print(' THIS IS A ROCK, PAPER AND SCISSORS GAME.')
print ("Please select an option.")
Rock = "R"
Paper = "P"
Scissors = "S"

while True :
    userChoice = input ("Choose (R(rock), P(paper), S(scissors):")
    possibleChoice = ["R", "P", "S"]
    computerChoice = random.choice (possibleChoice)
    print (f"\n Player: {userChoice}\n")
    print (f"\n CPU: {computerChoice}.\n")
    
    if userChoice == computerChoice:
        print (f'Both players selected {userChoice}.')
        print ('It is a tie!')
    elif userChoice == "R":
        if computerChoice == "S":
            print("Rock smashes scissors!")
            print ("You win!" )
        else:
            print("Paper covers rock! You lose.")
    elif userChoice == "P":
        if computerChoice == "R":
            print ("Paper covers rock!")
            print ("You win!")
        else:
            print ("Scissors cuts paper!")
            print ("You lose.")
    elif userChoice == "S":
        if computerChoice == "P":
            print ("Scissors cuts paper!")
            print ("You win!")
        else:
            print ("Rock smashes scissors!")
            print ("You lose.")  

    playAgain = input ("Play again?  (y/n):")
    if playAgain.lower () == "y":
       
        print ("Keep playing.")
    elif playAgain.lower () != "y":
        print ("Thank you for playing.")
        sys.exit
        break