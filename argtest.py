trace = False


def rangetest(**argchecks):
    return argtest(argchecks, lambda arg, vals: arg < vals[0] or arg > vals[1])


def typetest(**argchecks):
    return argtest(argchecks, lambda arg, type: not isinstance(arg, type))


def valuetest(**argchecks):
    return argtest(argchecks, lambda arg, tester: not tester(arg))


def argtest(argchecks, failif):
    def onDecorator(func):
        if not __debug__:
            return func
        else:
            code = func.__code__
            expected = list(code.co_varnames[:code.co_argcount])
            def onError(argname, criteria):
                errfmt = '%s argument "%s" not %s'
                raise TypeError(errfmt % (func.__name__, argname, criteria))

            def onCall(*pargs, **kargs):
                positionals = expected[:len(pargs)]
                for (argname, criteria) in argchecks.items():
                    if argname in kargs:
                        if failif(kargs[argname], criteria):
                            onError(argname, criteria)
                    elif argname in positionals:
                        position = positionals.index(argname)
                        if failif(pargs[position], criteria):
                            onError(argname, criteria)
                    else:
                        if trace:
                            print('Argument {} defaulted'.format(argname))
                return func(*pargs, **kargs)
            return onCall
    return onDecorator


if __name__ == '__main__':
    import sys


    def fails(test):
        try:
            result = test()
        except:
            print('[{}]'.format(sys.exc_info()[1]))
        else:
            print('?{}?'.format(result))


    print('-' * 60)


    @rangetest(m=(1, 12), d=(1, 31), y=(1900, 2013))
    def date(m, d, y):
        print('date = {}/{}/{}'.format(m, d, y))


    date(1, 2, 1960)
    fails(lambda: date(1, 2, 3))


    @typetest(a=int, c=float)
    def sum(a, b, c, d):
        print(a + b + c + d)


    sum(1, 2, 3.0, 4)
    sum(1, d=4, b=2, c=3.0)
    fails(lambda: sum('spam', 2, 99, 4))
    fails(lambda: sum(1, d=4, b=2, c=99))
    print('-' * 60)


    @valuetest(word1=str.islower, word2=(lambda x: x[0].isupper()))
    def msg(word1='mighty', word2='Larch', label='The'):
        print('{} {} {}'.format(label, word1, word2))


    msg()
    msg('majestic', 'Moose')
    fails(lambda: msg('Giant', 'Redwood'))
    fails(lambda: msg('great', word2='elm'))
    print('-' * 60)


    @valuetest(A=lambda x: isinstance(x, int), B=lambda x: x > 0 and x < 10)
    def manual(A, B):
        print(A + B)


    manual(100, 2)
    fails(lambda: manual(1.99, 2))
    fails(lambda: manual(100, 20))
    print('-' * 60)


    @rangetest(X=(1, 10))
    @typetest(Z=str)
    def nester(X, Y, Z):
        return ('{}-{}-{}'.format(X, Y, Z))


    print(nester(1, 2, 'spam'))
    fails(lambda: nester(1, 2, 3))
    fails(lambda: nester(1, 2, Z=3))
    fails(lambda: nester(0, 2, 'spam'))
    fails(lambda: nester(X=0, Y=2, Z='spam'))
