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

