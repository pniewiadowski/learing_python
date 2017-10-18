class ListInstance:
    """
    Mix-in class that provides a formatted print() or str() fo instances via inheritance of __str__ coded here; displays instance attrs only;
    self is instance of lowest class; __x names avoid clashing with client's attrs
    """

    def __attrnames(self):
        result = ''
        for attr in sorted(self.__dict__):
            result += '\t%s=%s\n' % (attr, self.__dict__[attr])
        return result

    def __str__(self):
        return '<Instance of %s(%s), address %s:\n%s>' % (
            self.__class__.__name__, self.__supers(), id(self), self.__attrnames())

    def __supers(self):
        names = []
        for super in self.__class__.__bases__:
            names.append(super.__name__)
        return ', '.join(names)


if __name__ == '__main__':
    import testmixin

    testmixin.tester(ListInstance)
