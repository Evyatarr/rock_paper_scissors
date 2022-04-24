import random

rounds = 0
wins = 0


def welcome_screen():
    global rounds
    num_of_rounds = input("Welcome to Rock Paper Scissors!\nChoose how many rounds you want to play:\na)1\nb)3\nc)5\n")
    if num_of_rounds == "a":
        rounds = 1
    elif num_of_rounds == "b":
        rounds = 3
    elif num_of_rounds == "c":
        rounds = 5
    else:
        print("error2")
        welcome_screen()
    user_action_choice(rounds)


def user_action_choice(chosen_rounds):
    for i in range(chosen_rounds):
        users_input = int(input("Choose:\n1.Rock\n2.Paper\n3.Scissors\n"))
        if 0 < users_input < 4:
            if users_input == 1:  # 1 = Rock
                game(1)
            elif users_input == 2:  # 2 = Paper
                game(2)
            elif users_input == 3:  # 3 = Scissors
                game(3)
        else:
            print("error!1")
            user_action_choice(rounds)
    win_announcement()


def game(choice):
    global wins
    cpu_choice = random.randint(1, 3)
    if choice == 1 and cpu_choice == 1:
        print("Rock vs Rock! It's a tie :(")
    elif choice == 1 and cpu_choice == 2:
        print("Rock vs Paper! You lose :(")
        wins -= 1
    elif choice == 1 and cpu_choice == 3:
        print("Rock vs Scissors! You Win :)")
        wins += 1
    elif choice == 2 and cpu_choice == 1:
        print("Paper vs Rock! You win :)")
        wins += 1
    elif choice == 2 and cpu_choice == 2:
        print("Paper vs Paper! it's a tie :(")
    elif choice == 2 and cpu_choice == 3:
        print("Paper vs Scissors! You lose :(")
        wins -= 1
    elif choice == 3 and cpu_choice == 1:
        print("Scissors vs Rock! You lose :(")
        wins -= 1
    elif choice == 3 and cpu_choice == 2:
        print("Scissors vs Paper! You win :)")
        wins += 1
    elif choice == 3 and cpu_choice == 3:
        print("Scissors vs Scissors! It's a tie :(")


def win_announcement():
    if wins > 0:
        users_choice = input("You won the game!\nDo you want to play again? (y/n)")
        if users_choice == 'y':
            welcome_screen()
    elif wins < 0:
        users_choice = input("You lost the game!\nDo you want to play again? (y/n)")
        if users_choice == 'y':
            welcome_screen()
    elif wins == 0:
        users_choice = input("It's a tie!\nDo you want to play again? (y/n)")
        if users_choice == 'y':
            welcome_screen()
    else:
        print("error3")


welcome_screen()
