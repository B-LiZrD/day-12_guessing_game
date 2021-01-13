from art import logo

print(logo)

import random

print("I'm thinking of a number between 1 and 100.")
answer = list(range(1, 101))

COMP_ANSWER = random.choice(answer)
# print(f"This is the comp answer {COMP_ANSWER}")

difficulty = input("Choose a difficulty: Type 'easy' or 'hard': ")
tries = 0
if difficulty == 'easy':
    tries = 10
elif difficulty == 'hard':
    tries = 5
else:
    print("Invalid input...You lose!")

print(f"You have {tries} tries left.")


def guessing_game():
    global COMP_ANSWER
    global tries
    resume = True
    while resume:
        guess = int(input("Make a guess: "))
        if guess == COMP_ANSWER:
            print("Congratulations, you guessed it")
            resume = False
        elif guess < COMP_ANSWER:
            print("Guess higher")
            tries -= 1
            print(f"You have {tries} tries left")
            if tries == 0:
                print("You ran out of guesses. I'm sorry, but you lose...(hehe)")
                resume = False
        elif guess > COMP_ANSWER:
            print("Guess lower")
            tries -= 1
            print(f"You have {tries} tries left")
            if tries == 0:
                print("You ran out of guesses. I'm sorry, but you lose...(hehe)")
                resume = False


guessing_game()