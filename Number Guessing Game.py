import random

print('Hello! This is a basic number guessing game')
number = random.randint(1, 100)
tries = 5

while tries > 0:
    guess = int(input('Guess a number between 1 and 100: '))
    
    if guess < number:
        tries -= 1
        print('Wrong! The number is higher than your guess.')
        print('Your tries left:', tries)
    elif guess > number:
        tries -= 1
        print('Wrong! The number is lower than your guess.')
        print('Your tries left:', tries)
    else:
        print('Congratulations! You guessed the correct number:', number)
        break
    
    if tries == 0:
        print('Game over! The number was:', number)

        print('Better luck next time!')
