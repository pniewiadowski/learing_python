import sys, time
force = list

class timer:
    def __init__(self, func):
        self.func = func
        self.alltime = 0
    def __call__(self, *args, **kwargs):
        start = time.clock()
        result = self.func(*args, **kwargs)
        elapsed = time.clock() - start
        self.alltime += elapsed
        print('{}: {%.5f}, {%.5f}'.format(self.func.__name__, elapsed, self.alltime))
        return result
@timer
def listcomp(N):
    return [x*2 for x in range (N)]
@timer
def mapcall(N):

