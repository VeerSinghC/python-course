import random

numbers = [3, 8, 15, 22, 35, 42, 50]
print("Available numbers:", numbers)

chosen_number = random.choice(numbers)

while True:
    guess = int(input("Guess the number chosen by the judge: "))

    if guess == chosen_number:
        print("Correct! You guessed the number.")
        break
    elif guess > chosen_number:
        print("Too high! Try a smaller number.")
    else:
        print("Too low! Try a bigger number.")
