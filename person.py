class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRasie(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def __repr__(self):
        return '[Person: %s %s]' % (self.name, self.pay)

class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)
    def giveRasie(self, percent, bonus=.10):
        Person.giveRasie(self, percent+bonus)

if __name__ == '__main__':
    # slef-test code
    bob = Person('Bob Smith')
    sue = Person('Sue Jons', job='dev', pay=100000)
    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName())
    sue.giveRasie(.10)
    print(sue)
    tom = Manager('Tom Jones', 50000)
    tom.giveRasie(.10)
    print(tom.lastName())
    print(tom)
    print('--All there--')
    for obj in (bob, sue, tom):
        obj.giveRasie(.10)
        print(obj)
        
