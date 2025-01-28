from Bank import Bank
import csv

def main():
    account = Bank.get()
    with open('accounts.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:

            if account.n_account in row:
                r = input('This account has exist, you want make a deposit here? ')

                while r.upper() not in 'YN':
                    r = input('This account has exist, you want make a deposit here? ')

                if r.upper() in 'Y':
                    account.deposit(int(input('Valor: ')))

                elif r.upper() in 'N':
                    r = input('You want make a windrow here?[Y/N] ')

                    while r.upper() not in 'YS':
                        r = input('You want make a windrow here?[Y/N] ')

                    if r.upper() in 'Y':
                        account.deposit(int(input('Valor: ')))
                    else:
                        print('Create a new account for progress')

if __name__ == '__main__':
    main()