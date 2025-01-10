#Guessing Game
import random

#Make sure both variables are integers.
def numberguesser():
    print("Welcome this is NumberGuesser.io!")
    print("You are trying to guess the random number.")
    print("Select your difficulty.")
    difficulty = int(input("Select easy(1), medium(2), or hard(3)"))
    print("Good Luck!")
    if difficulty == 1:
        guess = int(input("Enter Number 1-3"))
        secret = random.randint(1,3)
        if guess == secret:
            print("Congrats you guessed the right number!")
        else:
            print("You did not guess the right number. The right number was " + str(secret) + ".")
    elif difficulty == 2:
        guess = int(input("Enter Number 1-10"))
        secret = random.randint(1,10)
        if guess == secret:
            print("Congrats you guessed the right number!")
        else:
            print("You did not guess the right number. The right number was " + str(secret) + ".")
    elif difficulty == 3:
        guess = int(input("Enter Number 1-100"))
        secret = random.randint(1,100)
        if guess == secret:
            print("Congrats you guessed the right number!")
        else:
            print("You did not guess the right number. The right number was " + str(secret) + ".")
    again = int(input("Would you like to play again? Yes(1) or No(0)"))
    if again == 1:
        numberguesser()
    if again == 0:
        print("Thank you for playing.")

numberguesser()
