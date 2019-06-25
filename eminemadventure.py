
playagain = "yes"
print("start")

while playagain == "yes" or playagain == "Yes":
    userChoice = input("It is a nice day in LA.  You see posters advertising Eminem's new concert and want to go see it with your friends.  Buy the expensive tickets online (type 'Fandango') or look for the shady scalper at the venue (type 'scalper')? ")
    if userChoice == "Fandango" or userChoice == "fandango":
        print("Good choice!  You and your friends break the bank on tickets, but have an amazing time at the concert!")
        print("Congrats! You made the right choice and had the night of your life!")
        playagain = input("Would you like to try again? Type yes or no. ")
    elif userChoice == "scalper":
        print("You arrive at the concert venue and look for the man who looks strangely like three children stacked together in a trenchcoat.")
        print("You approach the scalper -- Vincent -- and ask to buy the goods.")
        print("He obliges, and you hand him the money.")
        print("Vincent congratulates you on your purchase and points to the entrance to the stage")
        print("You and your friends make your way excitedly to the concert, except when you get there, the concert is not as you expected.")
        print("You made the wrong choice.  The scalper misheard you and sold you front-row tickets to the M&M's concert!")
        playagain = input("Would you like to try again? Type yes or no. ")
        
    else:
        print("Please type either 'Fandango' or 'scalper'. ")
        playagain = input("Would you like to try again? Type yes or no. ")
    if playagain == "no":
        quit()

playagain == "yes" or playagain == "Yes"
while playagain == "yes" or playagain == "Yes":
    userChoice = input("You and your friends have so much fun at the concert that you don't realize that it is 3 o'clock in the morning.  You are all getting tired and hungry.  Do you go to McDonald's for an early breakfast (type "hungry") or do you decide to call it a day and go home (type "tired")? "
    if userChoice == "tired":
        print("Good choice!  You go home and get some much needed sleep.  You can always go to McDonald's another time!")
        playagain = input("Would you like to try again? Type yes or no. ")
    elif userChoice == "hungry":
        print("You decide to go to McDonald's because you and your friends are seriously starving. ")
        print("You have more than enough money to buy everything on the menu.")
        print("Your friends decide to try to eat everything on the menu in one sitting.")
        userChoice = input("Do you join in on the fast-food feast (type "yum") or do you decline to join their artery-clogging session (type "health")? ")
        if userChoice == "yum":
            print("You decide to join the fast-food feeding frenzy and eat everything you can.")
            print("You ate with ease, consuming four big macs, an m&m mcflurry, twenty-three chicken nuggets, and two orders of fries without flinching.  ")
            print("Once your hunger faded, however, you looked on in horror as your friends continued to shovel burgers and fries with little regard to their stomachs.  ")
            print("Your stomach and wallet ached, and you immensely regretted your excursion to McDonald's.  ")
            playagain = input("Would you like to try again?  Type yes or no. ")
        elif userChoice == "health":
            print("You decide to spare your health from the ravages of a McDonald's feast. ")
            print("You settle on ordering a modest 10pc chicken nuggets and watch on in humor as your friends bite off more than they can chew. ")
            print("You made the right decision.  You spared your health and wallet from the greasy terror of McDonald's. ")
            playagain = input("Would you like to try again?  Type yes or no. ")
        else:
            print("Please type either "health" or "yum".)
            playagain = input("Would you like to try again?  Type yes or no. ")