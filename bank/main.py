from Bank import Bank

def main():
    account = Bank.get()
    account.check()
    account.deposit(1000)
    account.windrow(100)
    account.append()
if __name__ == '__main__':
    main()