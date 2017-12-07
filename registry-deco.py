registry = {}


def register(obj):
    registry[obj.__name__] = obj
    return obj


@register
def spam(x):
    return (x ** 2)


@register
def ham(x):
    return (x ** 3)


@register
class Eggs:
    def __init__(self, x):
        self.data = x ** 4

    def __str__(self):
        return str(self.data)


print('Registry:')
for name in registry:
    print(name, '=>', registry[name], type(registry[name]))

print('\nManual calls:')
print(spam(2))
print(ham(2))
X = Eggs(2)
print(X)

print('\nRegistry calls:')
for name in registry:
    print(name, '=>', registry[name](2))
