
# CONSTANTS
HUNDRED_BILL = 100
FIFTY_BILL = 50
TWENTY_BILL = 20
TEN_BILL = 10
FIVE_BILL = 5

#American Exclusive oooooo
TWO_BILL = 2
ONE_BILL = 1

def CountCanadianBills(hundreds, fiftys, twentys, tens, fives):
    totalHundreds = hundreds * HUNDRED_BILL
    totalFiftys = fiftys * FIFTY_BILL
    totalTwentys = twentys * TWENTY_BILL
    totalTens = tens * TEN_BILL
    totalFives = fives * FIVE_BILL

    totalAmount = totalHundreds + totalFiftys + totalTwentys + totalTens + totalFives

    return totalAmount

def CountAmericanBills(hundreds, fiftys, twentys, tens, fives, twos, ones):
    totalHundreds = hundreds * HUNDRED_BILL
    totalFiftys = fiftys * FIFTY_BILL
    totalTwentys = twentys * TWENTY_BILL
    totalTens = tens * TEN_BILL
    totalFives = fives * FIVE_BILL
    totalTwos = twos * TWO_BILL

    totalAmount = totalHundreds + totalFiftys + totalTwentys + totalTens + totalFives + totalTwos + ones

    return totalAmount

if __name__ == '__main__':

    currencyChecker = input('What bill currency are you counting? (U)SA, (C)anada: ')

    if not currencyChecker.isalpha() and not currencyChecker.count > 1 :
        print('Not a single character or alphabettical!')
    else:

        currencyChecker = currencyChecker.upper()

        if currencyChecker == 'U':
            print('Counting American Bills')
            myHundreds = input('How many 100 dollar bills: ')
            myFiftys = input('How many 50 dollar bills: ')
            myTwentys = input('How many 20 dollar bills: ')
            myTens = input('How many 10 dollar bills: ')
            myFives = input('How many 5 dollar bills: ')
            myTwos = input('How many 2 dollar bills: ')
            myOnes = input('How many 1 dollar bills: ')
            total = CountAmericanBills(int(myHundreds), int(myFiftys), int(myTwentys), int(myTens), int(myFives), int(myTwos), int(myOnes))
            print(f'Total amount of cash is: $ {total} USD')
        elif currencyChecker == 'C':
            print('Counting Canadian Bills')
            myHundreds = input('How many 100 dollar bills: ')
            myFiftys = input('How many 50 dollar bills: ')
            myTwentys = input('How many 20 dollar bills: ')
            myTens = input('How many 10 dollar bills: ')
            myFives = input('How many 5 dollar bills: ')
            total = CountCanadianBills(int(myHundreds), int(myFiftys), int(myTwentys), int(myTens), int(myFives))
            print(f'Total amount of cash is: $ {total} CAD')
        else:
            print('Letter must be one of the available choices!')    


        
    