class Spam:
    numInstaces = 0

    def __init__(self):
        Spam.numInstaces += 1

    def printNumInstances(cls):
        print('Number of instances created: %s %s' % cls.numInstaces, cls)

    printNumInstances = classmethod(printNumInstances)


class Sub(Spam):
    def printNumInstances(cls):
        print('Extra stuff...', cls)
        Spam.printNumInstances()

    printNumInstances = classmethod(printNumInstances)
