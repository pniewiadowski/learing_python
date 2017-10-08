class Methods(object):
    def imeth(self, x):
        print([self, x])

    @staticmethod
    def smeth(x):
<<<<<<< HEAD
        print(x)
=======
        print([x])
>>>>>>> 851b808031f44624692f1fb5a70f5baaa8dea7c0

    @classmethod
    def cmeth(cls, x):
        print([cls, x])

    @property
    def name(self):
<<<<<<< HEAD
        return 'Bob ' + self.__class__.__name__
=======
        return 'Bob' + self.__class__.__name__
>>>>>>> 851b808031f44624692f1fb5a70f5baaa8dea7c0
