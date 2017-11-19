# class Powers:
#     def __init__(self, square, cube):
#         self._square = square
#         self._cube = cube
#
#     def getSquare(self):
#         return self._square ** 2
#
#     def setSquare(self, value):
#         self._square = value
#
#     square = property(getSquare, setSquare)
#
#     def getCube(self):
#         return self._cube ** 3
#
#     cube = property(getCube)
#
#
# X = Powers(3, 4)
# print(X.square)
# print(X.cube)
# X.square = 5
# print(X.square)

# class DescSquare:
#     def __get__(self, instance, owner):
#         return instance._square ** 2
#
#     def __set__(self, instance, value):
#         instance._square = value
#
#
# class DescCube:
#     def __get__(self, instance, owner):
#         return instance._cube ** 3
#
#
# class Powers:
#     square = DescSquare()
#     cube = DescCube()
#
#     def __init__(self, square, cube):
#         self._square = square
#         self._cube = cube
#
#
# X = Powers(3, 4)
# print(X.square)
# print(X.cube)
# X.square = 5
# print(X.square)

# class Powers:
#     def __init__(self, square, cube):
#         self._square = square
#         self._cube = cube
#
#     def __getattr__(self, item):
#         if item == 'square':
#             return self._square ** 2
#         elif item == 'cube':
#             return self._cube ** 3
#         else:
#             raise AttributeError(item)
#
#     def __setattr__(self, key, value):
#         if key == 'square':
#             self.__dict__['_square'] = value
#         else:
#             self.__dict__[key] = value
#
#
# X = Powers(3, 4)
# print(X.square)
# print(X.cube)
# X.square = 5
# print(X.square)

class Powers:
    def __init__(self, square, cube):
        self._square = square
        self._cube = cube

    def __getattribute__(self, item):
        if item == 'square':
            return object.__getattribute__(self, '_square') ** 2
        elif item == 'cube':
            return object.__getattribute__(self, '_cube') ** 3
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key == 'square':
            object.__setattr__(self, 'square', value)
        else:
            object.__setattr__(self, key, value)


X = Powers(3, 4)
print(X.square)
print(X.cube)
X.square = 5
print(X.square)
