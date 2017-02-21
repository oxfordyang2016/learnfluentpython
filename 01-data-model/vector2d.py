from math import hypot
#this is a class expmale
#how to implement operator + - * / abs
class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)



def testfunction():
    '''
    this is designed by myself
    >>> v = Vector(3, 4)
    >>> abs(v)
    5.0
    >>> v * 3
    Vector(9, 12)
    >>> abs(v * 3)
    15.0
    
    '''