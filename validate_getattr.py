class CardHolder:
    acctlen = 8
    retirage = 59.5

    def __init__(self, acct, name, age, addr):
        self.acct = acct
        self.name = name
        self.age = age
        self.addr = addr

    def __getattr__(self, item):
        if item == 'acct':
            return self._acct[:-3] + '***'
        elif item == 'remain':
            return self.retirage - self.age
        else:
            raise AttributeError(item)

    def __setattr__(self, key, value):
        if key == 'name':
            value.lower().replace(' ', '_')
        elif key == 'age':
            if value < 0 or value > 150:
                raise ValueError('invalid age')
        elif key == 'acct':
            name = '_acct'
            value = value.replace('-', '')
            if len(value) != self.acctlen:
                raise TypeError('invalid acct number')
        elif key == 'remain':
            raise TypeError('can not set remain')
        self.__dict__[key] = value
