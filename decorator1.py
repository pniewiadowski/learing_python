class tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func

    def __call__(self, *args):
        self.calls += 1
        print('call {} to {}'.format(self.calls, self.func.__name__))
        self.func(*args)


@tracer
def spam(a, b, c):
    print(a + b + c)