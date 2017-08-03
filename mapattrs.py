import pprint


def trace(X, label='', end='\n'):
    print(label + pprint.pformat(X) + end)


def filterdictvals(D, V):
    """
    dict D with enteris for value V removed/
    filterdictvals(dict(a=1, b=2, c=1),1) => {'b':2}
    :param D:
    :param V:
    :return:
    """
    return {K: V2 for (K, V2) in D.items() if V2 != V}


def inverdict(D):
    """
    dict D with values changed to keys (groupd by values)
    Values must all be hashable to work as dict/set keys.
    invertdict(dict(a=1, b=2, c=1)) => {1: ['a'', 'c'], 2: ['b']}
    :param D:
    :return:
    """

    def keysof(V):
        return sorted(K for K in D.keys() if D[K] == V)

    return {V: keysof(V) for V in set(D.values())}


def dflr(cls):
    """Classic depth-first left-to-right order of class tree at cls.
    Cycles not possible: Python disallows on __bases__ changes."""
    here = [cls]
    for sup in cls.__bases__:
        here += dflr(sup)
    return here


def inheritance(instance):
    """Inheritance order squence: new-style (MRO) or classic (DFLR)"""
    if hasattr(instance.__class__, '__mro__'):
        return (instance,) + instance.__class__.__mro__
    else:
        return [instance] + dflr(instance.__class__)


def mapattrs(instance, withobject=False, bysource=False):
    """dict with keys giving all inherited attributes of instance,
    with value giving the object that each is inherited from.
    withobject: False=remove object built-in class attributes
    bysource: True=group result by object instead of attributes.
    Support classes with slots that preclude __dict__ in instances."""
    attr2obj = {}
    inherits = inheritance(instance)
    for attr in dir(instance):
        for obj in inherits:
            if hasattr(obj, '__dict__') and attr in obj.__dict__:
                attr2obj[attr] = obj
                break
    if not withobject:
        attr2obj = filterdictvals(attr2obj, object)
    return attr2obj if not bysource else inverdict(attr2obj)


if __name__ == '__main__':
    print('Classic classes in 2.X, new style in 3.X')


    class A: attr1 = 1


    class B(A): attr2 = 2


    class C(A): attr1 = 3


    class D(B, C): pass


    I = D()
    print('Py=>%s' % I.attr1)
    trace(inheritance(I), 'INH\n')
    trace(mapattrs(I), 'ATTRS\n')
    trace(mapattrs(I, bysource=True), 'OBJS\n')

    print('New-style classes in 2.X and 3.X')


    class A(object): attr1 = 1


    class B(A): attr2 = 2


    class C(A): attr1 = 3


    class D(B, C): pass


    I = D()
    print('Py=>%s' % I.attr1)

    trace(inheritance(I), 'INH\n')
    trace(mapattrs(I), 'ATTRS\n')
    trace(mapattrs(I, bysource=True), 'OBJS\n')
