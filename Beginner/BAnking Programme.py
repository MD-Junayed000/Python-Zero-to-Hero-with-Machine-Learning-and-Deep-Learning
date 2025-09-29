# Banking Programme
# 1. Show Balance 2.Deposit 3. Withdraw

def show_balance(balance):
    print(f'Your balance is : {balance:.2f}')


def deposit():
    amount=float(input('Enter your Deposit amount: '))

    if amount<0:
        print('Invalid amount deposited')
        return 0

    else:
        return amount

def withdraw(balance):
    amount=float(input('Enter the amount to be with drawn: '))

    if amount>balance:
        print('Insufficient Funds')
        return 0

    elif amount<0:
        print('Ur a Gorib')
        return 0

    else:
        return amount
def main():

    balance=0 ## main() function nh dile  global variable so can be used in functions also
    is_running=True

    while is_running:
        print('Banking Programme')
        print('1.Show Balance')
        print('2.Deposit')
        print('3.Withdraw')
        print('4.Exit')

        choice=input('Enter your choice (1-4): ')

        if choice=='1':
            show_balance(balance)

        elif choice=='2':
            balance+=deposit()

        elif choice=='3':
            balance-=withdraw(balance)
        elif choice=='4':
            is_running=False

        else:
            print('That is not a valid choice')


    print('Thank you have a nice Family')

if __name__=='__main__':
    main()
