'''Implementar o nome do cliente,
 validação via email,
  usar regex'''


import csv
import random

class Bank:
    def __init__(self, n_account, password, balance=0):
        self.n_account = n_account
        self.password = password
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

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        if str(password).isnumeric() or str(password).isalpha():
            raise ValueError('This password have number and words')
        if len(password) != 6:
            raise ValueError('This password have 6 elements')
        self._password = password

    @classmethod
    def create(cls):
        nums = (1, 2, 3, 4, 5, 6, 7, 8, 9)
        num_account = ''
        for _ in range(8):
            nums_account = random.choices(nums, k=8)

        num_account = ''.join(map(str, nums_account))

        psswrd = input('Password: ')
        password = input('Confirm: ')
        while password != password:
            print('Password incorrect!')
            psswrd = input('Password: ')
            password = input('Confirm: ')

        return cls(num_account, password)

    def check(self):
        with open('accounts.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:

                if self.n_account in row:

                    password = input('This account has exist, write a password: ')

                    if password == self._password:

                        r = input('You want make a deposit here? ')

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

                    else:
                        raise ValueError('Invalid Password')

    def append(self):
        with open('accounts.csv', "r", newline="", encoding="utf-8") as csvfile:
            reader = list(csv.reader(csvfile))
            header = reader[0]
            rows = reader[1:]

        new_list = []
        balance = 0

        for row in rows:
            if str(self.n_account) == row[0]:
                balance = float(row[2])
            else:
                new_list.append(row)

        with open('accounts.csv', "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(header)
            writer.writerows(new_list)

        with open('accounts.csv', "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([self.n_account, self.password, self._balance + balance])

    def deposit(self, n):
        self._balance += n

    def windrow(self, n):
        self._balance -= n

    def __str__(self):
        return f'Number of account: {self._n_account}\nBalance: {self._balance}'
