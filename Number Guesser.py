import random


def game(choice):
    random_int = random.randint(0, 14)

    if choice == random_int:
        print("You guessed it!")
        quit()
    else:
        print("Try again")
        prompt()


def test_user_entry(choice):
    if choice.isdigit():
        choice = int(choice)

        if choice <= 0:
            print("Please enter a number greater than 0")
            prompt()
        else:
            game(choice)
    else:
        print("Numbers only please!")
        prompt()


def prompt():
    choice = input("Choose a number ")
    test_user_entry(choice)


prompt()
