def rangetest(*argchecks):
    def onDecorator(func):
        if not __debug__:
            return func
        else:
            def onCall(*args):
                for (ix, low, high) in argchecks:
                    if args[ix] < low or args[ix] > high:
                        errsmg = 'Arguments {} not in {}...{}'.format(ix, low, high)
                        raise TypeError(errsmg)
                return func(*args)

            return onCall
    return onDecorator
