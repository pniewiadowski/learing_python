class AttrSquare:
    def __init__(self, start):
        self.value = start

    def __getattr__(self, item):
        if item == 'X':
            return self.value ** 2
        else:
            raise AttributeError(item)

    def __setattr__(self, key, value):
        if key == 'X':
            key = 'value'
        self.__dict__[key] = value


A = AttrSquare(3)
B = AttrSquare(32)
print(A.X)

A.X = 4
print(A.X)
print(B.X)
