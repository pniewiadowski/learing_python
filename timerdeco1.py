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
        print('{}: {:5f}, {:5f}'.format(self.func.__name__, elapsed, self.alltime))
        return result


@timer
def listcomp(N):
    return [x * 2 for x in range(N)]


@timer
def mapcall(N):
    return force(map((lambda x: x * 2), range(N)))


result = listcomp(5)
listcomp(50000)
listcomp(500000)
listcomp(1000000)
print(result)
print('allTime = {}'.format(listcomp.alltime))

print('')
result = mapcall(5)
mapcall(50000)
mapcall(500000)
mapcall(1000000)
print(result)
print('allTime = {}'.format(mapcall.alltime))
print('\n**map\com = {}'.format(round(mapcall.alltime / listcomp.alltime, 3)))
