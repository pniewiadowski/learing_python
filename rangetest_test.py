from rangetest import rangetest


@rangetest(age=(0, 120))
def persinfo(name, age):
    print('{} is {} years old'.format(name, age))


@rangetest(M=(1, 12), D=(1, 31), Y=(0, 2013))
def birthday(M, D, Y):
    print('birthday = {0}/{1}/{2}'.format(M, D, Y))


persinfo('Bob', 40)
persinfo(age=40, name='Bob')
birthday(5, D=1, Y=1963)


# persinfo('Bob', 150)
# persinfo(age=150, name='Bob')
# birthday(5, D=40, Y=1963)

class Person:
    def __init__(self, name, job, pay):
        self.job = job
        self.pay = pay

    @rangetest(percent=(0.0, 1.0))
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))


bob = Person('Bob Smith', 'dev', 10000)
sue = Person('Sue Jones', 'dev', 10000)
bob.giveRaise(.10)
sue.giveRaise(percent=.20)
print(bob.pay, sue.pay)


# bob.giveRaise(1.10)
# sue.giveRaise(percent=1.2)

@rangetest(a=(1, 10), b=(1, 10), c=(1, 10), d=(1, 10))
def omitargs(a, b=7, c=8, d=9):
    print(a, b, c, d)


omitargs(1, 2, 3, 4)
omitargs(1, 2, 3)
omitargs(1, 2, 3, d=4)
omitargs(1, d=4)
omitargs(d=4, a=1)
omitargs(1, b=2, d=4)
omitargs(d=8, c=7, a=1)

# omitargs(1, 2, 3, 11)
# omitargs(1, 2, 11)
# omitargs(1, 2, 3, d=11)
# omitargs(11, d=4)
# omitargs(d=4, a=11)
# omitargs(1, b=11, d=4)
# omitargs(d=8, c=7, a=11)
