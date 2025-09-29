# python slot machine
import random
def spin_row():
    symbols=['🤣','🍎','💊','🫶']

    results=[]### empty list of result

    ''' for symbol in range(3):
        results.append(random.choice(symbols))
    return results '''
    return [random.choice(symbols) for symbol in range(3)]


def print_row(row):
    print(' '.join(row)) ### join each element in the list by space as mentioned


def get_payout(row,bet):

    if row[0]==row[1]==row[2]:
        if row[0]=='🍎':
            return bet*3
    else:
        return 0

def main():
    balance=100
    print('Welcome to python Slot')
    print('Symbol: 🫶💊🍎🤣')
    while balance>0:
        print(f'Current balance is {balance}')
        bet=input('Place your bet amount: ')

        if not bet.isdigit():
            print('Invalid amoount and type agian')
            continue ### get out from current iteration

        bet=int(bet)

        if bet>balance:
            print('Insufficient funds')
            continue

        if bet<=0:
            print('Bet must be greater')
            continue

        balance-=bet
        row=spin_row()
        print('Spinning...\n')
        print_row(row)

        payout=get_payout(row,bet)

        if payout>0:
            print(f'You won {payout}')

        else:
            print('Sorry u fucking lost')

        balance+=payout

        play_again=input('do you want to play again: ').upper()
        if play_again!='Y':
            break

if __name__=='__main__':
    main()