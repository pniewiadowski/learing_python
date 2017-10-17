class MyList:
    def __init__(self, start):
        # self.wrapped = start[:]
        self.wrapped = list(start)

    def __add__(self, other):
        return MyList(self.wrapped + other)

    def __mul__(self, time):
        return MyList(self.wrapped * time)

    def __getitem__(self, offset):
        return self.wrapped[offset]

    def __len__(self):
        return len(self.wrapped)

    def append(self, node):
        self.wrapped.append(node)

    def __getattr__(self, name):
        return getattr(self.wrapped, name)

    def __repr__(self):
        return repr(self.wrapped)


if __name__ == '__main__':
    x = MyList('spam')
    print(x)
    print(x[2])
    print(x[1:])
    print(x + ['eggs'])
    print(x * 3)
    x.append('a')
    x.sort()
    print(' '.join(c for c in x))
