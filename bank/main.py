from Bank import Bank

def main():
    print('='*40)
    print(f'{"[1] Access your account":^40}')
    print(f'{"[2] Create a new account":^40}')
    print('='*40)
    solicitation = input('-> ')

    while solicitation not in '12':
        solicitation = input('-> ')

    if solicitation == '1':
        account = Bank.get()
        account.check()
        account.append()
    if solicitation == '2':
        account = Bank.create()
        account.append()


if __name__ == '__main__':
    main()