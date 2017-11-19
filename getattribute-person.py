class Person:
    def __init__(self, name):
        self._name = name

    def __getattribute__(self, item):
        print('get: ' + item)
        if item == 'name':
            item = '_name'
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        print('set: ' + key)
        if key == 'name':
            key = '_name'
        self.__dict__[key] = value

    def __delattr__(self, item):
        print('del: ' + item)
        if item == 'name':
            item = '_name'
        del self.__dict__[item]


bob = Person('Bob Smith')
print(bob.name)
bob.name = 'Robert Smith'
print(bob.name)
del bob.name
print('-' * 20)
sue = Person('Sue Jones')
print(sue.name)
