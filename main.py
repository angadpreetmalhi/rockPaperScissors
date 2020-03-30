
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
    print(compChoice)
    if userChoice == compChoice:
        print("Tie, Both got zero point\n ")
    # if user enter p (paper)
    elif userChoice == "p" and compChoice == "s":
        compPoints = compPoints + 1
        print(f"Your guess is {userChoice} and computer guess is {compChoice} \n")
        print("Computer won 1 point \n")
        print(f"Computer Points = {compPoints} and Your points = {userPoints} \n ")
    elif userChoice == "p" and compChoice == "r":
        userPoints = userPoints + 1
        print(f"Your guess {userChoice} and Computer guess is {compChoice} \n")
        print("You won 1 point \n")
        print(f"Computer points = {compPoints} and Your points = {userPoints} \n")

    # if user enter r (rock)
    elif userChoice == "r" and compChoice == "p":
        compPoints = compPoints + 1
        print(f"your guess {userChoice} and computer guess is {compChoice} \n")
        print("computer won 1 point \n")
        print(f"Computer points = {compPoints} and Your points = {userPoints} \n")
    elif userChoice == "r" and compChoice == "s":
        userPoints = userPoints + 1
        print(f"your guess {userChoice} and computer guess is {compChoice} \n")
        print("You won 1 point \n")
        print(f"Computer points = {compPoints} and Your points = {userPoints} \n")

    # if user enter s(scissors)
    elif userChoice == "s" and compChoice == "p":
        userPoints = userPoints + 1
        print(f"your guess {userChoice} and computer guess is {compChoice} \n")
        print("You won 1 point \n")
        print(f"Computer points = {compPoints} and Your points = {userPoints} \n")
    elif userChoice == "s" and compChoice == "r":
        compPoints = compPoints + 1
        print(f"your guess {userChoice} and computer guess is {compChoice} \n")
        print("computer won 1 point \n")
        print(f"Computer points = {compPoints} and Your point = {userPoints} \n")
    #if user enter something else
    else:
        print("Wrong Input!\n")
        compPoints = compPoints + 1
        print(f"Computer points = {compPoints} and Your points = {userPoints} \n")

    noOfChance = noOfChance + 1
    print(f"{chance - noOfChance} is left out of {chance} \n")
print("Game over")
if compPoints == userPoints:
    print("Tie")
elif compPoints > userPoints:
    print("Computer won and you lost")
else:
    print("You won and Computer lost")
print(f"Computer's point = {compPoints} and Your point = {userPoints} \n")


