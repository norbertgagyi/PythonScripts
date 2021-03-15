import webbrowser, sys, pyperclip

adress = ''

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

print(sys.argv)

webbrowser.open('https://www.google.com/maps/place/' + address)
