print("Let's play Rock Paper Scissors")

user_input = input("Rock, Paper, or scissors?")
user_input = user_input.lower()

robot = ""

if user_input == "rock":
    robot = "Paper"
elif user_input == "paper":
    robot = ""
