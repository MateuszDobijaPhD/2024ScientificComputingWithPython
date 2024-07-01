# EXERCISE 9.2 (SCATTER)
#
# Generate n=100 random points in a unit square [0,1]x[0,1]. Points are green if the distance from (0,0) is less then 1;
# they are red otherwise. The marker area of a point (x,y) should be proportional to |x|+|y|.

import numpy as np
import matplotlib.pyplot as plt


def distance(x_coordinate, y_coordinate):
    return np.sqrt(x_coordinate**2 + y_coordinate**2)


def marker_size(x_coordinate, y_coordinate):
    return np.fabs(x_coordinate) + np.fabs(y_coordinate)


def get_max_marker_size(markers_sizes):
    return max(markers_sizes)

def normalized_marker_size(x_coordinate, y_coordinate, max_marker_size):
    return (np.fabs(x_coordinate) + np.fabs(y_coordinate))/max_marker_size


def normalized_marker_size_per_list(markers_sizes, max_marker_size):
    const_multiplier = 1000
    for i in range(noOfPoints):
        markers_sizes[i] = const_multiplier*(markers_sizes[i] / max_marker_size)**2
    return markers_sizes

def getColors(x, y, noOfPoints):
    colors = []
    for i in range(noOfPoints):
        if distance(x[i],y[i]) < 1:
            colors.append('g')
        else:
            colors.append('r')
    return colors

def getAreas(x,y, noOfPoints):
    areas = []
    for i in range(noOfPoints):
        areas.append(marker_size(x[i], y[i]))
    maxArea = get_max_marker_size(areas)
    areas = normalized_marker_size_per_list(areas, maxArea)
    return areas

noOfPoints = 100 #1000 can be used to see that colour based on distance is correct
x = np.random.uniform(0, 1, noOfPoints)
y = np.random.uniform(0, 1, noOfPoints)
colors = getColors(x,y, noOfPoints)
areas =getAreas(x,y, noOfPoints)
plt.scatter(x, y, s=areas, c=colors, alpha=0.5)
plt.title("random point with sizes related to |x|+|y|")
plt.xlabel("x")
plt.ylabel("y")
plt.show()