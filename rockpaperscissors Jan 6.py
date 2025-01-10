#Rock Paper Scissors
#Phoenix Ling

#Init
import random

#Functions
wins = 0
losses = 0
draws = 0
roundnumber = 1

def game():
    while True:
        global wins
        global losses
        global draws
        global roundnumber
        playerchoice = input("Choose rock, paper, or scissors:")
        while True:
            if playerchoice == "rock" or playerchoice == "paper" or playerchoice == "scissors":
                break
            else:
                print("Choose a valid input:")
                playerchoice = input("Choose rock, paper, or scissors:")
        aichoice = random.randint(1,3)
        if aichoice == 1:
            aichoice = "rock"
        elif aichoice == 2:
            aichoice = "paper"
        else:
            aichoice = "scissors"
        if playerchoice == "rock" and aichoice == "rock":
            print("Both selections were rock resulting in a draw.")
            draws = draws + 1
        elif playerchoice == "paper" and aichoice == "paper":
            print("Both selections were paper resulting in a draw.")
            draws = draws + 1
        elif playerchoice == "scissors" and aichoice == "scissors":
            print("Both selections were scissors resulting in a draw.")
            draws = draws + 1
        elif playerchoice == "rock" and aichoice == "scissors":
            print("You chose rock and the computer chose scissiors resulting in you winning!")
            wins = wins + 1
        elif playerchoice == "rock" and aichoice == "paper":
            print("You chose rock and the computer chose paper resulting in you losing...")
            losses = losses + 1
        elif playerchoice == "paper" and aichoice == "rock":
            print("You chose paper and the computer chose rock resulting in you winning!")
            wins = wins + 1
        elif playerchoice == "paper" and aichoice == "scissors":
            print("You chose paper and the computer chose scissors resulting in you losing...")
            losses = losses + 1
        elif playerchoice == "scissors" and aichoice == "paper":
            print("You chose scissors and the computer chose paper resulting in you winning!")
            wins = wins + 1
        elif playerchoice == "scissors" and aichoice == "rock":
            print("You chose scissors and the computer chose rock resulting in you losing...")
            losses = losses + 1
        print("Right now you have " + str(wins) + " wins, " + str(losses) + " losses, and " + str(draws) + " draws.")
        print("Would you like to play again?")
        playagain = input("yes or no")
        roundnumber = roundnumber + 1
        if playagain == "yes":
            print(" ")
            print("Round " + str(roundnumber))
        elif playagain == "no":
            print(" ")
            print("Thank you for playing!")
            break
#Main
print("Welcome to Rock Paper Scissors")
print("Select rock, paper, or scissors")
game()
