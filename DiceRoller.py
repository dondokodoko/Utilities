# Random dice rolling python program
from random import randint

rollAgain = True

MIN_DICE_SIZE = 6
MAX_DICE_SIZE = 20

while rollAgain != False:
    diceSize = input('What size dice do you want to roll: ')
    numberOfTimesToRollDice = input('How many times would you like to roll this dice: ')

    if diceSize.isnumeric() and numberOfTimesToRollDice.isnumeric():
        numericNumberOfTimeToRollDice = int(numberOfTimesToRollDice)
        numericDiceSize = int(diceSize)
        if numericDiceSize >= MIN_DICE_SIZE and numericDiceSize <= MAX_DICE_SIZE:
            for i in range(numericNumberOfTimeToRollDice):
                print(f'Roll {i + 1}: {randint(1, numericDiceSize)}')
            rollAgain = False
        else:
            print(f"Dice value must be between {MIN_DICE_SIZE} and {MAX_DICE_SIZE}!")
    else:
        print('Dice value must be numeric')

