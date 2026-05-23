import random

from colorama import Fore, Style

win_conditions = {
    1: 3,
    2: 1,
    3: 2
}

value_to_choice = {
    1: "Rock",
    2: "Paper",
    3: "Scissors"
}

points_player = 0
points_computer = 0

while True:

    choice = int(input(Style.RESET_ALL + "Choose:\n1: Rock\n2: Paper\n3: Scissors\n>>> "))

    computer_choice = random.randint(1, 3)

    print(Fore.BLUE + f"Computer chose {value_to_choice[computer_choice]}")

    if win_conditions[choice] == computer_choice:
        print(Fore.GREEN + "You win.")
        points_player += 1
    elif win_conditions[computer_choice] == choice:
        print(Fore.RED + "You lost.")
        points_computer += 1
    else:
        print(Fore.YELLOW + "Tie")

    print(f"Score: {points_player} : {points_computer}")

    if input(Fore.BLUE + "Play again? y/n\n>>> ") != 'y':
        print("bye")
        break
