MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1


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


def main():
    balance = deposit()
    lines = get_num_of_lines()
    while True:
        bet = get_bets()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"Bet cannot be the given amount as you do not have enough balance. Your current balance is "
                  f"{balance}.")
        else:
            break

    print(f"You are betting ${bet} on each lines which is a total${total_bet}.")
    print(balance, lines)


main()
