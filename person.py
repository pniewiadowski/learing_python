class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRasie(self, percent):
        self.pay = int(self.pay * (1 + percent))


if __name__ == '__main__':
    # slef-test code
    bob = Person('Bob Smith')
    sue = Person('Sue Jons', job='dev', pay=100000)
    print(bob.name, bob.pay)
    print(sue.name, sue.job, sue.pay)
    print(bob.lastName(), sue.lastName())
    sue.giveRasie(.10)
    print(sue.pay)
    print(sue)
