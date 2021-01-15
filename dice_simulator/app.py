import random

repeat = 'y'
while repeat == 'y':
    number = random.randint(1,6)
    if number == 1:
        print(' ___________')
        print('|           |')
        print('|           |')
        print('|     O     |')
        print('|           |')
        print('|___________|\n')

    if number == 2:
        print(' ___________')
        print('|           |')
        print('|     O     |')
        print('|           |')
        print('|     O     |')
        print('|___________|\n')

    if number == 3:
        print(' ___________')
        print('|           |')
        print('|     O     |')
        print('|     O     |')
        print('|     O     |')
        print('|___________|\n')

    if number == 4:
        print(' ___________')
        print('|           |')
        print('|  O     O  |')
        print('|           |')
        print('|  O     O  |')
        print('|___________|\n')

    if number == 5:
        print(' ___________')
        print('|           |')
        print('|  O     O  |')
        print('|     O     |')
        print('|  O     O  |')
        print('|___________|\n')

    if number == 6:
        print(' ___________')
        print('|           |')
        print('|  O     O  |')
        print('|  O     O  |')
        print('|  O     O  |')
        print('|___________|\n')

    repeat = input("Enter 'y' to roll again:    ")