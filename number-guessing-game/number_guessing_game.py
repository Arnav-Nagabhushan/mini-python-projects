import random

print('Welcome to Number Guessing Game!')
print('\nI am thinking of a number between 1 and 100')

def start_game():
    secret_number = random.randint(1, 100)
    guesses = 0

    while True:
        guess = input('\nEnter your guess: ')

        try:
            guess = int(guess)
            guesses += 1

            if guess > secret_number:
                print('Too high! Try again.')

            elif guess < secret_number:
                print('Too low! Try again.')

            else:
                print(f'🎉 Correct! You guessed the number in {guesses} guesses!')
                print('Thanks for playing!')

                break

        except ValueError:
            print('Please enter a valid number.')

def main():
    start_game()

if __name__ == "__main__":
    main()
