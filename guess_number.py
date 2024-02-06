number = 10

print("I'm thinking of a number...")
while True:
    guess = input("What number am I thinking of? ")
    if guess == 'q':
        print(f"You quit! The number was {number}.")
        break
    elif int(guess) == number:
        print("Congratulations! You guessed the right number.")
        break
    elif int(guess) > number:
        print("Your guess is too high. Try again.")
    else:
        print("Your guess is too low. Try again.")
