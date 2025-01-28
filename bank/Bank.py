import csv

class Bank:
    def __init__(self, n_account, balance=0):
        self.n_account = n_account
        self._balance = balance

    @property
    def n_account(self):
        return self._n_account

    @n_account.setter
    def n_account(self, n_account):
        if len(n_account) != 8:
            raise ValueError("Invalid account, it's number valid is 8")

        if not str(n_account).isnumeric():
            raise ValueError("Invalid account, words isn't accept")

        self._n_account = n_account

    @classmethod
    def get(cls):
        num_account = input('Number of account: ')
        return cls(num_account)

    def check(self):
        with open('accounts.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:

                if self.n_account in row:
                    r = input('This account has exist, you want make a deposit here? ')

                    while r.upper() not in 'YN':
                        r = input('This account has exist, you want make a deposit here? ')

                    if r.upper() in 'Y':
                        self.deposit(int(input('Valor: ')))

                    elif r.upper() in 'N':
                        r = input('You want make a windrow here?[Y/N] ')

                        while r.upper() not in 'YS':
                            r = input('You want make a windrow here?[Y/N] ')

                        if r.upper() in 'Y':
                            self.deposit(int(input('Valor: ')))
                        else:
                            print('Create a new account for progress')

    def append(self):
        with open('accounts.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if self.n_account in row:
                    raise ValueError('This number of account has exist')

        with open('accounts.csv', '+a') as file:
            header = ['Number Account', 'Balance']
            writer = csv.DictWriter(file, fieldnames=header)
            writer.writeheader()
            writer.writerow({'Number Account': self.n_account, 'Balance': self._balance})


    def deposit(self, n):
        self._balance += n

    def windrow(self, n):
        self._balance -= n

    def __str__(self):
        return f'Number of account: {self._n_account}\nBalance: {self._balance}'
