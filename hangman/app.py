import random
import re

def hangman():
    word = random.choice(['ironman', 'superman', 'batman', 'wonderwoman', 'thor', 'hulk', 'captainamerica', 'falcon', 'blackpanther'])
    valid_letters = re.compile('[a-zA-Z]')
    turns = 10

    guess_word = ''

    while len(word)>0:
        main = ''
        missed = 0

        for letter in word:
            if letter in guess_word:
                main = main + letter
            else:
                main = main + "_" + " "

        if main == word:
            print(main)
            print('You won!')
            break

        print('Guess the word:', main)
        guess = input()

        if valid_letters.match(guess):
            guess_word = guess_word + guess
        else:
            print('Enter a valid character')
            guess = input()

        if guess not in word:
            turns = turns - 1
            if turns == 9:
                print('9 turns left')
                print('------------')
            if turns == 8:
                print('8 turns left')
                print('------------')
                print('    O      ')
            
            if turns == 7:
                print('7 turns left')
                print('------------')
                print('    O      ')
                print('    |      ')
            if turns == 6:
                print('6 turns left')
                print('------------')
                print('    O      ')
                print('    |      ')
                print('   /      ')
            if turns == 5:
                print('5 turns left')
                print('------------')
                print('    O      ')
                print('    |      ')
                print('   / \     ')
            if turns == 4:
                print('4 turns left')
                print('------------')
                print('  \ O      ')
                print('    |      ')
                print('   / \     ')
            if turns == 3:
                print('3 turns left')
                print('------------')
                print('  \ O /    ')
                print('    |      ')
                print('   / \     ')
            if turns == 2:
                print('2 turns left')
                print('------------')
                print('  \ O /|   ')
                print('    |      ')
                print('   / \     ')
            if turns == 1:
                print('1 turn left')
                print('------------')
                print('  \ O_|/    ')
                print('    |      ')
                print('   / \     ')
            if turns == 0:
                print('You lose')
                print('------------')
                print('    O_|    ')
                print('   /|\      ')
                print('   / \     ')
                break

name = input('Please enter your name to start the game: ')
print(f'Welcome, {name}')
print('Try to guess the word in less than 10 attempts\n')

hangman()
# word = random.choice(['ironman', 'superman', 'batman', 'wonderwoman', 'thor', 'hulk', 'captainamerica', 'falcon', 'blackpanther'])
# print(word)
# valid_letters = re.compile('[a-zA-Z]')

# print(valid_letters.match('a'))
# print(re.search(valid_letters, 'abcd'))

