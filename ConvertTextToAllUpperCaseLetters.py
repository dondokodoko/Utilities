
wantsToRestart = ''

def capitalizeTitle():
    title = input('Enter text: \t')
    print('\t\t' + title.upper())

while wantsToRestart != 'n':
    capitalizeTitle()
    wantsToRestart = input('\n\nWould you like to convert another text? (y/n): \t')
