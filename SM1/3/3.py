class NoPositionalArgsError(Exception):
    pass


class UnsuccessfulChaseError(Exception):
    pass


def chase(*args, speed=2):
    lst = []
    if not args:
        raise NoPositionalArgsError('Too few arguments')
    if speed == 0:
        raise ZeroDivisionError('Zero speed')

    for i in args:
        if len(i) % speed == 0:
            lst.append(i)
    lst.sort(key=len, reverse=True)
    if not lst:
        raise UnsuccessfulChaseError("We didn't catch up with anyone")
    return lst


data = ('Nikitsky Gates', 'Arbatskaya Square', 'Ostozhenka',
        'Kropotkinskaya')
print(chase(*data))

data = ('Kitay Gorod', 'Chistye Prudy', 'Vasilievsky Fall')
print(chase(*data, speed=3))
