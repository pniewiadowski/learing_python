class MyError(Exception):
    pass


def oops():
    raise MyError('Spam')


def dommed():
    try:
        oops()
    except IndexError:
        print('cought and index error')
    except MyError as data:
        print('caught error', MyError, data)
    else:
        print('no error caught...')


if __name__ == '__main__':
    dommed()
