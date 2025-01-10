#Multiplication Quiz
#Phoenix Ling

#Init
import random
#Function
def quiz():
    while True:#Loops the whole thing to play infinitley until decided not to.
        correct = 0
        incorrect = 0
        difficulty = input("Select easy, medium, or hard:")#This allows for the student to select how hard the questions will be.
        while True: #Makes sure students difficulty level selection is a valid one.
                if difficulty == "easy" or difficulty == "medium" or difficulty == "hard":
                    break
                else:
                    print("Choose a valid input:")
                    difficulty = input("Choose easy, medium, or hard:")
        length = int(input("Now choose the amount of questions you would like to answer:"))#This variable is how many questions the quiz length will be.
        print("You may now begin your quiz")
        for i in range(length):
            if difficulty == "easy": #Each if statement here will change the two numbers being multiplied depending on the difficulty.
                firstnumber = random.randint(1,5)
                secondnumber = random.randint(1,5)
            elif difficulty == "medium":
                firstnumber = random.randint(1,10)
                secondnumber = random.randint(1,10)
            elif difficulty == "hard":
                firstnumber = random.randint(1,20)
                secondnumber = random.randint(1,20)
            print("What is " + str(firstnumber) + " x " + str(secondnumber) + "?")#Displays question
            answer = firstnumber * secondnumber
            studentanswer = int(input("Enter your answer here:"))
            if answer == studentanswer: #These if statements display whether the student answered the question correctly.
                print("Great job!")
                correct = correct + 1
            elif answer != studentanswer:
                print("Incorrect...")
                print("The correct answer was " + str(answer))
                incorrect = incorrect + 1
        amountofquestions = correct + incorrect
        finalscore = correct/amountofquestions*100 #Calculates final score
        print("Your final score was an " + str(finalscore) + "%(" + str(correct) + "/" + str(amountofquestions) + ".)")#Displays final score.
        print("Would you like to go again?")
        playagain = input("Choose yes or no.")
        if playagain == "yes":
            print(" ")
            motivation = random.randint(1,5) #This section displays motivational phrases everytime a student chooses to play again.
            if motivation == 1:
                print("Keep going!")
            elif motivation == 2:
                print("You're on a roll!")
            elif motivation == 3:
                print("You're doing great!")
            elif motivation == 4:
                print("Yayyyyy")
            elif motivation == 5:
                print("Wow you're still going?!")
        elif playagain == "no":
            print(" ")
            print("Thank you for playing!")
            break #This break allows for the student to play endlessly and choose when they want to stop.


#Main
print("Hello, welcome to the multiplication quiz!")#Introduces the quiz to the student.
print("Answer the questions as they appear on your screen.")
print("Please select your difficulty level and quiz length, then you may start.")
quiz()
