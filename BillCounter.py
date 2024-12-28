
# CONSTANTS
HUNDRED_BILL = 100
FIFTY_BILL = 50
TWENTY_BILL = 20
TEN_BILL = 10
FIVE_BILL = 5

def CountBills(hundreds, fiftys, twentys, tens, fives):
    print(f'Hundred Bills: {hundreds}')
    print(f'Fifty Bills: {fiftys}')
    print(f'Twenty Bills: {twentys}')
    print(f'Ten Bills: {tens}')
    print(f'Five Bills: {fives}')

    totalHundreds = hundreds * HUNDRED_BILL
    totalFiftys = fiftys * FIFTY_BILL
    totalTwentys = twentys * TWENTY_BILL
    totalTens = tens * TEN_BILL
    totalFives = fives * FIVE_BILL

    totalAmount = totalHundreds + totalFiftys + totalTwentys + totalTens + totalFives

    return totalAmount


if __name__ == '__main__':

    myHundreds = input('How many 100 dollar bills: ')
    myFiftys = input('How many 50 dollar bills: ')
    myTwentys = input('How many 20 dollar bills: ')
    myTens = input('How many 10 dollar bills: ')
    myFives = input('How many 5 dollar bills: ')

    total = CountBills(int(myHundreds), int(myFiftys), int(myTwentys), int(myTens), int(myFives))

    print(f'Total amount of cash is: $ {total} CAD')