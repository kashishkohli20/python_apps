import json
from difflib import get_close_matches

data = json.load(open('data.json'))

def search_word(word):
    # w = w.lower()
    if word.lower() in data:
        return data[word.lower()]
    elif word.capitalize() in data:
        return data[word.capitalize()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        confirmation = input(f'Did you mean {get_close_matches(word, data.keys())[0]} instead? Y or N:')
        if confirmation == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif confirmation == "n":
            return "Word not found....."
        else:
            return "Please check confirmation"
    else:
        return 'Word not found...'


req = 'y'

while(req == 'y'):
# print(data['aircraft'])
    word = input('Please enter the word to search: ')

    print(word.title())
    print(word.capitalize())
    output = search_word(word)

    if(type(output) == list):
        print(*output, sep='\n')
    else:
        print(output)

    req = input('Do you want to make a new search? [y/n]: ')

