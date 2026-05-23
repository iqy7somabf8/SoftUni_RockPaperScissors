import random

win_conditions = {
    1: 3,
    2: 1,
    3: 2
}

while True:

    choice = int(input("Choose:\n1: Rock\n2: Paper\n3: Scissors\n>>> "))

    computer_choice = random.randint(1, 3)

    print(f"Computer chose {computer_choice}")

    if win_conditions[choice] == computer_choice:
        print("You win.")
    elif win_conditions[computer_choice] == choice:
        print("You lost.")
    else:
        print("Tie")

    print("Play again? Y/N")

    if input() != 'Y':
        print("bye")
        break
