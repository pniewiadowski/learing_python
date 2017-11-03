def oops():
    raise IndexError()


def doomed():
    try:
        oops()
    except IndexError:
        print('cought an index error!')
    else:
        print('no error cought!')


if __name__ == '__main__':
    doomed()
