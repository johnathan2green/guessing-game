import random

def guess(x):
    random_number = random.randint(1, x)
    tries = 0 
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Try again. The number you guessed is too low!')
        elif guess > random_number:
            print('Try again. The number you guessed is too high.')
        tries = tries + 1

    print(f'Yes! The correct number was {random_number}!');
    print(f'It took you {tries} tries!');
    
guess(10)
