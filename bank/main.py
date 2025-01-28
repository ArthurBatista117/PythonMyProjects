from Bank import Bank

def main():
    account = Bank.get()
    account.deposit(int(input('Deposit: ')))
    account.windrow(50)
    print(account.__str__())


if __name__ == '__main__':
    main()