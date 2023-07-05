import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3
symbols_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbols_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_winnings(values, lines, bet, columns):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        f_symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if f_symbol != symbol_to_check:
                break
        else:
            winnings = values[f_symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines


def get_slot_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for i in range(symbol_count):
            all_symbols.append(symbol)
    cols_symbols = []
    for _ in range(cols):
        col_sym = []
        cp_sym = all_symbols.copy()
        for _ in range(rows):
            val = random.choice(cp_sym)
            cp_sym.remove(val)
            col_sym.append(val)
        cols_symbols.append(col_sym)
    return cols_symbols


def print_slot_mac(columns):
    for row in range(ROWS):
        for col in range(COLS):
            if col < COLS-1:
                print(columns[col][row], end=' | ')
            else:
                print(columns[col][row])


def deposit():
    while True:
        amount = input("How much would you like to enter($)? ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 1.")
        else:
            print("Please enter a number.")
    return amount


def get_num_of_lines():
    while True:
        lines = input(f"How many lines would like to bet on(1-{str(MAX_LINES)})? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")
    return lines


def get_bets():
    while True:
        bet = input(f"How much would you like bet on each line({str(MIN_BET)}-{str(MAX_BET)})? ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print("Enter a valid number of bets.")
        else:
            print("Please enter a number.")
    return bet


def play(balance):
    lines = get_num_of_lines()
    while True:
        bet = get_bets()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"Bet cannot be the given amount as you do not have enough balance. Your current balance is "
                  f"{balance}.")
        else:
            break
    print(f"You're betting a total of ${total_bet}  on {lines} lines.")
    slots = get_slot_spin(ROWS, COLS, symbols_count)
    print_slot_mac(slots)
    winnings, winning_lines = check_winnings(symbols_value, lines, bet, slots)
    print(f"You won ${winnings}")
    print(f"You won on lines: ", *winning_lines)
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}.")
        spin = input("Press enter to play (q to quit).")
        if spin == 'q':
            print(f"You have left with ${balance}")
            break
        else:
            if balance != 0:
                balance += play(balance)
            else:
                opt = input("You have run out of balance. If you would like to play again please enter 'y'(enter-quit)")
                if opt == 'y':
                    main()
                else:
                    break


main()
