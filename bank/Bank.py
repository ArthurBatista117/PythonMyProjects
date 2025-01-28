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

    def deposit(self, n):
        self._balance += n

    def windrow(self, n):
        self._balance -= n

    def __str__(self):
        return f'Number of account: {self._n_account}\nBalance: {self._balance}'
