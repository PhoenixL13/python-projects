def madlibs():
    while True:
        print("Welcome to Madlibs That Will Make You Mad!")
        print("Please enter your choices for each question:")
        name1 = input("Please enter a name:")
        adjective1 = input("Please enter an adjective:")
        animal1 = input("Please enter an animal:")
        verb1 = input("Please enter a verb:")
        location1 = input("Please enter a location:")
        emotion1 = input("Please enter an emotion:")
        name2 = input("Please enter another name:")
        adjective2 = input("Please enter another adjective:")
        verb2 = input("Please enter another verb:")
        location2 = input("Please enter another location:")
        emotion2 = input("Please enter another emotion:")
        print("Creating story.........")
        print("One day " + adjective1 + " " + name1 + " and ")
        print(adjective2 + " " + name2 + " decided to go to go on a side quest to ")
        print(location1 + ". They had to " + verb1 + " before they could leave which made them ")
        print(emotion1 + ". After " + verb1 + "ing, " + adjective1 + " " + name1 + " and ")
        print(adjective2 + " " + name2 + " started their journey to ")
        print(location1 + ". On the way they stopped at " + location2)
        print("to pick up some supplies. Once arriving at " + location1 + " they ran into a ")
        print(animal1 + " leaving them in a(n) " + emotion2 + " state. In order to fight it they")
        print(verb2 + " until the " + animal1 + " ran away. Then " + adjective1 + " ")
        print(name1 + " and " + adjective2 + " " + name2 + " decided to never go on a side quest again.")
        print("Hope you enjoyed the story!")
        selection = int(input("Enter (1) to go again and (2) to quit:"))
        if selection == 1:
            print("You may now go again!")
        elif selection == 2:
            print("Thanks for trying out Madlibs That Will Make You Mad!")
            break



madlibs()

