number = 10
max_guesses = 5

print("I'm thinking of a number...")
for i in range(max_guesses, 0, -1):
    guess = input("What number am I thinking of? ")
    if guess == 'q':
        print(f"You quit! The number was {number}.")
        break
    elif int(guess) == number:
        print("Congratulations! You guessed the right number.")
        break
    elif int(guess) > number:
        print(f"Your guess is too high. Try again. You have {i-1} guesses left.")
    else:
        print(f"Your guess is too low. Try again. You have {i-1} guesses left.")
else:
    print(f"Sorry! You've run out of guesses. The number was {number}.")
