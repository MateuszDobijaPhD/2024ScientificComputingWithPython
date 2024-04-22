# EXERCISE 7.1
#
# Create a function find_axis(v1, v2) which returns the unit vector v3, where v3 is perpendicular to the vectors v1 and v2. If the vectors v1 and v2 are parallel (or zero) then the function should raise an exception (ValueError)
# [Hint: v1 and v2 are parallel if the cross product v1 × v2 is zero]. Vectors are instances of the Vector class from Homework 6.

def find_axis(v1, v2):