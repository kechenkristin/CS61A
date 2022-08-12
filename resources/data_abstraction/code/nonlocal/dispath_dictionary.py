def account(initial_balance):
    """ The dispatch function is a general method for implementing a message 
    passing interface for abstract data.

    >>> a = account(20)
    >>> deposit(a, 5)
    >>> withdraw(a, 17)
    >>> check_balance(a)
    8
    """
    def deposit(amount):
        dispatch['balance'] += amount
        return dispatch['balance']

    def withdraw(amount):
        if amount > dispatch['balance']:
            return 'Insufficient funds'
        dispatch['balance'] -= amount
        return dispatch['balance']

    dispatch = {'deposit': deposit,
                'withdraw': withdraw,
                'balance': initial_balance}

    return dispatch


def withdraw(account, amount):
    return account['withdraw'](amount)


def deposit(account, amount):
    return account['deposit'](amount)


def check_balance(account):
    return account['balance']
