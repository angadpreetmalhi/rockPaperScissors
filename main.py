#rock paper scissors
import random
# r =='rock', p =='paper', s=='scissors'
lst = ['r', 'p', 's']
chance = 6
noOfChance = 0
compPoints = 0
userPoints = 0
print("Rock,Paper,Scissors Game")
print("r for Rock \np for Paper \ns for Scissors")

# making the game in while
while noOfChance < chance:
    userChoice = input('Rock,Paper,Scissors:')
    compChoice = random.choice(lst)

    if userChoice == compChoice:
        print("Tie Both 0 point to each \n ")
    # if user enter p (paper)
    elif userChoice == "p" and compChoice == "s":
        compPoints = compPoints + 1
        print(f"your guess {userChoice} and computer guess is {compChoice} \n")
        print("computer wins 1 point \n")
        print(f"compPoints is {compPoints} and your point is {userPoints} \n ")
    elif userChoice == "p" and compChoice == "r":
        userPoints = userPoints + 1
        print(f"your guess {userChoice} and computer guess is {compChoice} \n")
        print("Human wins 1 point \n")
        print(f"compPoints is {compPoints} and your point is {userPoints} \n")

    # if user enter r (rock)
    elif userChoice == "r" and compChoice == "p":
        compPoints = compPoints + 1
        print(f"your guess {userChoice} and computer guess is {compChoice} \n")
        print("computer wins 1 point \n")
        print(f"compPoints is {compPoints} and your point is {userPoints} \n ")
    elif userChoice == "r" and compChoice == "s":
        userPoints = userPoints + 1
        print(f"your guess {userChoice} and computer guess is {compChoice} \n")
        print("Human wins 1 point \n")
        print(f"compPoints is {compPoints} and your point is {userPoints} \n")

    # if user enter s(scissors)
    elif userChoice == "s" and compChoice == "p":
        userPoints = userPoints + 1
        print(f"your guess {userChoice} and computer guess is {compChoice} \n")
        print("Human wins 1 point \n")
        print(f"compPoints is {compPoints} and your point is {userPoints} \n")
    elif userChoice == "s" and compChoice == "r":
        compPoints = compPoints + 1
        print(f"your guess {userChoice} and computer guess is {compChoice} \n")
        print("computer wins 1 point \n")
        print(f"compPoints is {compPoints} and your point is {userPoints} \n ")
    #if user enter something else
    else:
        print("you have input wrong \n")
        compPoints = compPoints + 1
    noOfChance = noOfChance + 1
    print(f"{chance - noOfChance} is left out of {chance} \n")
print("Game over")
if compPoints == userPoints:
    print("Tie")
elif compPoints > userPoints:
    print("Computer wins and you loose")
else:
    print("you win and computer loose")
print(f"your point is {userPoints} and computer point is {compPoints}")


