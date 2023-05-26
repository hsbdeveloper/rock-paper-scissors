import random

userScore = 0
computerScore = 0

choice = ["rock", "paper", "scissors"]

while True:
    user = input("Please select rock, paper, scissors or Q to quit: ").lower()
    if user == "q":
        break
    if user not in choice:
        continue
    randomNumber = random.randint(0, 2)
    computer = choice[randomNumber]
    print("Computer picked", computer + ".")
    if user == "rock" and computer == "scissors":
        print("You won!")
        userScore += 1
    elif user == "paper" and computer == "rock":
        print("You won!")
        userScore += 1
    elif user == "scissors" and computer == "paper":
        print("You won!")
        userScore += 1
    else:
        print("You lost!")
        computerScore += 1

print("Goodbye!")