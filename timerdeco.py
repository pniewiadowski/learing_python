import time


def timer(label='', trace=True):
    def onDecorator(func):
        def onCall(*args, **kargs):
            start = time.clock()
            result = func(*args, **kargs)
            elapsed = time.clock() - start
            onCall.alltime += elapsed
            if trace:
                format = '%s%s: %.10f, %.10f'
                values = (label, func.__name__, elapsed, onCall.alltime)
                print(format % values)
            return result

        onCall.alltime = 0
        return onCall

    return onDecorator
