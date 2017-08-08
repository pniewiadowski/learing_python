class Spam:
    numInstaces = 0

    def __init__(self):
        Spam.numInstaces = Spam.numInstaces + 1

    def printNumInstances():
        print('Number of instances created: %s' % Spam.numInstaces)
