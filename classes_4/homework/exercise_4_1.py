# Let p=(x,y) be a point in a plane. Define the following functions using lambda:
# (a) a test if p is in unit (filled) circle,
# (b) a test if the coordinates of p are positive,
# (c) a sorting key (y decreasing, x increasing),
# (d) a sorting key (the sum |x|+|y|).
#
# Using tests: list(filter((lambda p: ...), point_list))
# Using sorting keys: point_list.sort(key=lambda p: ...)
#
import math

x = 4
y = 4
p = (x, y)
circle_x = 5
circle_y = 5
p2 = (circle_x, circle_y)
r1 = 5
point_list = [(1,2), (1,4), (1,1), (1,5), (5,3), (5,4), (-98, 98), (0, 5)]

isPInUnitCircle = lambda p, midOfTheCircle=p2, r=r1: (math.sqrt(((midOfTheCircle[0] - p[0])**2) + ((midOfTheCircle[1] - p[1])**2))) < r
areCoordinatesOfPPositive = lambda p: (p[0] > 0) and (p[1] > 0)
sortingKey1 = lambda p: (-p[1], p[0])
sortingKey2 = lambda p: (math.fabs(p[0]) + math.fabs(p[1]))

print(isPInUnitCircle(p, p2, r1))
print(areCoordinatesOfPPositive(p))
print(list(filter((isPInUnitCircle), point_list)))
print(list(filter((areCoordinatesOfPPositive), point_list)))
point_list.sort(key = sortingKey1)
print(point_list)
point_list.sort(key = sortingKey2)
print(point_list)