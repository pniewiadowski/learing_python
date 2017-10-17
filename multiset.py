from setwrapper import Set


class MuliSet(Set):
    """Inherits all Set names, but extends intesect and union to support mulitple operands; note that "self" is still
    the first argument (stored in the *args argument now); also note that the inherited & and | operators call the new
    methods here with 2 arguments, but processing more than 2 requires a method call, not an expression; intersect
    doesn't remove duplicates here: the Set constructor does;"""

    def intersect(self, *others):
        res = []
        for x in self:
            for other in others:
                if x not in other: break
            else:
                res.append(x)
        return Set(res)

    def union(*args):
        res = []
        for seq in args:
            for x in seq:
                if not x in res:
                    res.append(x)
        return Set(res)
