import webbrowser, sys, pyperclip

# check whether command line arguments were passed
if len(sys.argv) > 1:
    search_address = ' '.join(sys.argv[1:])
else:
    search_address = pyperclip.paste

webbrowser.open(f'https://www.google.com/maps/place/{search_address}')