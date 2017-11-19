class GetAttr:
    attr1 = 1

    def __init__(self):
        self.attr2 = 2

    def __getattr__(self, item):
        print('get: ' + item)
        if item == 'attr3':
            return 3
        else:
            raise AttributeError(item)


X = GetAttr()
print(X.attr1)
print(X.attr2)
print(X.attr3)

print('-' * 20)


class GetAttribute:
    attr1 = 1

    def __init__(self):
        self.attr2 = 2

    def __getattribute__(self, item):
        print('get: ' + item)
        if item == 'attr3':
            return 3
        else:
            return object.__getattribute__(self, item)


X = GetAttribute()
print(X.attr1)
print(X.attr2)
print(X.attr3)
