class Spam:
    numInstaces = 0

    def count(cls):
        cls.numInstaces += 1

    def __init__(self):
        self.count()

    count = classmethod(count)


class Sub(Spam):
    numInstaces = 0

    def __init__(self):
        Spam.__init__(self)


class Other(Spam):
    numInstaces = 0
