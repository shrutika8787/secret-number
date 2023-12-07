import random


def comp_guess(x):
    low = 1
    high = x
    feedback = ""
    print("Hey computer guess the number")
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(
            f"Is {guess} too high (H) or too low (L) or correct (C) :"
        ).lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1

    print(f"Yay! The computer guessed the number {guess} correctly.")


comp_guess(100)
