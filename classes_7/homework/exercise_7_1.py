# EXERCISE 7.1
#
# Create a function find_axis(v1, v2) which returns the unit vector v3, where v3 is perpendicular to the vectors v1 and
# v2. If the vectors v1 and v2 are parallel (or zero) then the function should raise an exception (ValueError)
# [Hint: v1 and v2 are parallel if the cross product v1 × v2 is zero]. Vectors are instances of the Vector class from Homework 6.

import math
from classes_6.homework.exercise_6_1 import Vector
def find_axis(v1, v2):
    if v1.isZero():
        raise ValueError("v1 is zero")
    if v2.isZero():
        raise ValueError("v2 is zero")
    if v1.isParallel(v2):
        raise ValueError("v1 is parallel to v2")
    v3 = v1.cross(v2)
    return v3.getUnitVector()

v1 = Vector(1, 2, 3)
v2 = Vector(1, 2, 4)

v3Unit = find_axis(v1, v2)
print("perpendicular vector:", v3Unit)