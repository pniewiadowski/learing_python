class MetaTwo(type):
    def __new__(meta, classname, supers, classdict):
        print('In MetaTwo.new: ', classname, supers, classdict, sep='\n...')
        return type.__new__(meta, classname, supers, classdict)

    def __init__(Class, classname, supers, classdict):
        print('In MetaTwo.init:', classname, supers, classdict, sep='\n...')
        print('...init class object:', list(Class.__dict__.keys()))


class Eggs:
    pass


print('making class')


class Spam(Eggs, metaclass=MetaTwo):
    data = 1

    def meth(self, arg):
        return self.data + arg


print('making instacne')
X = Spam()
print('data', X.data, X.meth(2))
