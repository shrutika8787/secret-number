import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}:"))
        if guess < random_number:
            print("Sorry guess again.Too Low")
        elif guess > random_number:
            print("Sorry guess again.Too high")
        else:
            print(f"Yay! Congrats you have guessed the secret number {random_number}")
            again = input(
                "If you want to play again type y else if you want to exit type n :"
            )
            if again == "y":
                random_number = random.randint(1, x)
                guess = 0
                continue
            else:
                break


guess(100)
