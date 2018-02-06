from timerdeco import timer
import sys

force = list if sys.version_info[0] == 3 else (lambda x: x)
print('-' * 80)


@timer(trace=True, label='[CCC]==>')
def listcomp(N):
    return [x * 2 for x in range(N)]


@timer('[MMM==>]')
def mapcall(N):
    return force(map((lambda x: x * 2), range(N)))


for func in (listcomp, mapcall):
    result = func(5)
    func(5000000)
    print(result)
    print('allTime = %s\n' % func.alltime)
print('-' * 80)


class Person:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    @timer()
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)

    @timer(label='**')
    def lastName(self):
        return self.name.split()[-1]


bob = Person('Bob Smith', 50000)
sue = Person('Sue Jones', 100000)
bob.giveRaise(.10)
sue.giveRaise(.20)
print(int(bob.pay), int(sue.pay))
print(bob.lastName(), sue.lastName())
print('%.5f %.5f' % (Person.giveRaise.alltime, Person.lastName.alltime))
