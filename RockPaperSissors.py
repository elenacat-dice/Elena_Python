import random
#test

def AlwaysWin(user_input):

    robot = ""

    if user_input == "rock":
        robot = "Paper"
    elif user_input == "paper":
         robot = "Scissors"
    elif user_input == "scissors":
        robot = "Rock"
    else:
       print("Invalid input. Valid inputs are:Rock, Paper, Scissors.")
    if not robot == "":
       print("We threw", robot, ".")
       print("Sorry You Lost:(")
    return

print ("Do you want to play Rock Paper Scissors? If yes type y if no type n")
user_input = input("y, or n").lower()
possible_options = ["y, or n"]
person = possible_options

if person == 'y':
    user_input = input("Rock, paper, or scissors?").lower()

    #AlwaysWin(user_input)

    possible_options = ["rock", "paper", "scissors"]
    robot = possible_options[random.randint(0,2)]
    print("Robot throws", robot)
    if robot == 'rock':
        if user_input == 'rock':
            print ("The robot played rock. We tied. Try again")
            print("would you like to play again? Type y for yes or n for no")
        elif user_input == 'paper':
            print("Robot played rock. You win! Congradulations! :D")
            print("would you like to play again? Type y for yes or n for no")
        elif user_input == 'scissors':
            print("The robot played rock. You lost. sorry :( ")
            print("would you like to play again? Type y for yes or n for no")
        else:
            print("Invalid input. Valid inputs are: Rock, Paper, Scissors.")

    if robot == 'paper':
        if user_input == 'paper':
            print ("The robot played paper. We tied. Try again")
            print("would you like to play again? Type y for yes or n for no")
        elif user_input == 'scissors':
            print("The robot played paper. You win! Congradulations! :D")
            print("would you like to play again? Type y for yes or n for no")
        elif user_input == 'rock':
            print("The robot played paper. You lost. sorry :( ")
            print("would you like to play again? Type y for yes or n for no")
        else:
            print("Invalid input. Valid inputs are: Rock, Paper, Scissors.")

    if robot == 'scissors':
        if user_input == 'scissors':
            print ("The robot played scissors. We tied. Try again")
            print("would you like to play again? Type y for yes or n for no")
        elif user_input == 'rock':
            print("The robot played scissors. You win! Congradulations! :D")
            print("would you like to play again? Type y for yes or n for no")
        elif user_input == 'paper':
            print("The robot played scissors. You lost. sorry :( ")
            print("would you like to play again? Type y for yes or n for no")
        else:
            print("Invalid input. Valid inputs are: Rock, Paper, Scissors.")
            print("would you like to play again? Type y for yes or n for no")
else:
    print("OK, Have a great day!")

