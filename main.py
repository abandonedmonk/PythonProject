import random

MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100

ROWS = 3
COLS = 3

symbolCount = {
    "$" : 2,
    "#" : 4,
    "@" : 6,
    "&" : 8
}

symbolValue = {
    "$" : 5,
    "#" : 4,
    "@" : 3,
    "&" : 2
}

def checkWinnings(columns, lines, bet, values):
    winnings = 0
    winningLines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns: 
            symbolToCheck = column[line]
            if symbol != symbolToCheck:
                break
        else:
            winnings += values[symbol] * bet
            winningLines.append(line + 1)
    return winnings, winningLines

def getSlotMachinePick(rows, cols, symbols):
    allSymbols = []
    for symbol, symbolCount in symbols.items():
        for _ in range (symbolCount):
            allSymbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        currentSymbols = allSymbols[:]
        for _ in range (rows):
            value = random.choice(currentSymbols)
            currentSymbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def printSlotMachine (columns):
    for row in range (len(columns[0])):
        for i,column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print() 


def deposit():
    while True:
        amount = input("How much amount do you want to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if (amount > 0):
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    return amount

def getNumberOfLines():
    while True:
        lines = input("How much lines do you want (1-" + str(MAX_LINES) + ")? " )
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= 3:
                break
            else:
                print("lines must be within the limit (1-" + str(MAX_LINES) + ").")
        else:
            print("Please enter a number.")
    return lines

def getBet():
    while True:
        amount = input("How much amount do you want to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between the limit ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")
    return amount

def spin(balance):
    lines = getNumberOfLines()
    while True:
        bet = getBet()
        totalBet = bet * lines
        if totalBet > balance:
            print(f"You do not have enough amount to bet. Your current balance is ${balance}")
        else: 
            break

    slots = getSlotMachinePick(ROWS, COLS, symbolCount)
    printSlotMachine(slots)
    winnings, winningLines = checkWinnings(slots, lines, bet, symbolValue)
    print(f"You won ${winnings}")
    print(f"You won on lines:", *winningLines)
    return winnings - totalBet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to spin (q to quit)")
        if answer == "q":
            break
        balance += spin(balance)
    print(f"You are left with ${balance}")

main()