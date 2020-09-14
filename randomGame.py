from random import randint
from sys import argv

answer = randint(int(argv[1]), int(argv[2]))

while True:
    try:
        guess = int(
            input(f'Please enter a number between {argv[1]} and {argv[2]} to guess: '))

        if guess == answer:
            print(f'You have won the guess game 🤩.')
            break
        else:
            print(f'Please try another guess, it is not the correct one 😢.')
            # print(f'your guess is {guess}, answer is {answer}.')
            continue

    except ValueError:
        print('Please enter a valid number.')
        continue
