traceMe = False


def trace(*args):
    if traceMe:
        print('[' + ' '.join(map(str, args)) + ']')


def accessControl(failIf):
    def onDecorator(aClass):
        class onInstance:
            def __init__(self, *args, **kwargs):
                self.__wrapped = aClass(*args, **kwargs)

            def __getattr__(self, key):
                trace('get:', key)
                if failIf(key):
                    raise TypeError('private attribute fetch: ' + key)
                else:
                    return getattr(self.__wrapped, key)

            def __setattr__(self, key, value):
                trace('set:', key, value)
                if key == '_onInstance__wrapped':
                    self.__dict__[key] = value
                elif failIf(key):
                    raise TypeError('private attribute change: ' + key)
                else:
                    setattr(self.__wrapped, key, value)

        return onInstance

    return onDecorator


def Private(*attributes):
    return accessControl(failIf=(lambda attr: attr in attributes))


def Public(*attributes):
    return accessControl(failIf=(lambda attr: attr not in attributes))
