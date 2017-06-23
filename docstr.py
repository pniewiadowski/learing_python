"I am: docstr.__doc__"

def func(args):
    "I am: docstr.func.__doc__"
    pass

class Spam:
    "I am: Spam.__doc__ or docstr.Spam.__doc__ or slef.__doc__"
    def methon(self):
        "I am: Spam.method.__doc__ or self.method.__doc__"
        print(self.__doc__)
        print(self.methon.__doc__)