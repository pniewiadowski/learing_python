class GetAttr:
    eggs = 88

    def __init__(self):
        self.spam = 77

    def __len__(self):
        print('__len__: 42')
        return 42

    def __getattr__(self, item):
        print('getattr: ' + item)
        if item == '__str__':
            return lambda *args: '[Getattr str]'
        else:
            return lambda *args: None


class GetAttribute:
    eggs = 88

    def __init__(self):
        self.spam = 77

    def __len__(self):
        print('__len__: 42')
        return 42

    def __getattribute__(self, item):
        print('getattribute: ' + item)
        if item == '__str__':
            return lambda *args: '[GetAttribute str]'
        else:
            return lambda *args: None


for Class in GetAttr, GetAttribute:
    print('\n' + Class.__name__.ljust(50, '='))

    X = Class()
    X.eggs
    X.spam
    X.other
    len(X)

    try:
        X[0]
    except:
        print('fail []')
    try:
        X + 99
    except:
        print('faile +')
    try:
        X()
    except:
        print('fail ()')
    X.__call__()
    print(X.__str__())
    print(X)
