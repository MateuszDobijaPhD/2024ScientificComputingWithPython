# EXERCISE 6.1
#
# Create 3D vectors as a Python class.
#
# class Vector:
#
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def __repr__(self): pass        # return string "Vector(x, y, z)"
#
#     def __eq__(self, other): pass   # v == w
#
#     def __ne__(self, other):        # v != w
#         return not self == other
#
#     def __add__(self, other): pass   # v + w
#         # Hint: return Vector(...)
#
#     def __sub__(self, other): pass   # v - w
#
#     def __mul__(self, other): pass  # return the dot product (number)
#
#     def cross(self, other): pass   # return the cross product (Vector)
#
#     def length(self): pass   # the length of the vector
#
#     def __hash__(self):   # we assume that vectors are immutable
#         return hash((self.x, self.y, self.z))   # recommended
#
# # Exemplary tests. Change values in your tests.
# import math
# v = Vector(1, 2, 3)
# w = Vector(2, -3, 2)
# assert v != w
# assert v + w == Vector(3, -1, 5)
# assert v - w == Vector(-1, 5, 1)
# assert v * w == 2
# assert v.cross(w) == Vector(13, 4, -7)
# assert v.length() == math.sqrt(14)
# S = set([v, v, w])
# assert len(S) == 2
#
# print("Tests passed")

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return "Vector({}, {}, {})".format(self.x, self.y, self.z)        # return string "Vector(x, y, z)"

    def __eq__(self, other):   # v == w
        return (self.x == other.x) and (self.y == other.y) and (self.z == other.z)

    def __ne__(self, other):        # v != w
        return not self == other

    def __add__(self, other):   # v + w
        newX = self.x + other.x
        newY = self.y + other.y
        newZ = self.z + other.z
        return Vector(newX, newY, newZ)

    # Hint: return Vector(...)

    def __sub__(self, other):   # v - w
        newX = self.x - other.x
        newY = self.y - other.y
        newZ = self.z - other.z
        return Vector(newX, newY, newZ)
    def __mul__(self, other):  # return the dot product (number)
        return (self.x * other.x) + (self.y * other.y) + (self.z * other.z)
    def cross(self, other):   # return the cross product (Vector)
        newX = self.y * other.z - self.z * other.y
        newY = self.z * other.x - self.x * other.z
        newZ = self.x * other.y - self.y * other.x
        return Vector(newX, newY, newZ)
    def length(self):   # the length of the vector
        return math.sqrt(pow(self.x, 2) + pow(self.y, 2) + pow(self.z, 2))
    def __hash__(self):   # we assume that vectors are immutable
        return hash((self.x, self.y, self.z))   # recommended

# Exemplary tests. Change values in your tests.
import math
v = Vector(1, 2, 3)
w = Vector(2, -3, 2)
print("vector v:", v)
print("vector w:", w)
assert v != w
assert v + w == Vector(3, -1, 5)
assert v - w == Vector(-1, 5, 1)
assert v * w == 2
assert v.cross(w) == Vector(13, 4, -7)
assert v.length() == math.sqrt(14)
S = set([v, v, w])
assert len(S) == 2

print("Tests passed")
