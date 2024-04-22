# EXERCISE 7.2
#
# Create the following infinite iterators:
# (a) returning 0, 1, 0, 1, 0, 1, ...,
# (b) returning randomly 0 or 1 on demand,
# (c) returning 0, 1, 0, -1, 0, 1, 0, -1, ...
import random
def iter_zeroes_ones():   # an infinite iterator
    i = 0
    step = 1
    while True:
        yield i%2
        i += step

def random_zeroes_ones():
    availableValues = [0, 1]
    while True:
        selectedValue = random.choice(availableValues)
        yield selectedValue

def iter_zeroes_ones_minus_ones():   # an infinite iterator
    i = 0
    step = 1
    useMinusSign = False
    while True:
        if(useMinusSign == True):
            yield -1*(i % 2)
            useMinusSign = False
        else:
            yield i%2
            useMinusSign = True
        i += step


#test iter_zeroes_ones
# startId = 0
# expectedNumberOfIterations = 100
# print("iter_zeroes_ones:")
#
# zeroesOnesGen = iter_zeroes_ones()
# for i in range(startId, expectedNumberOfIterations):
#     print("id of iteration: " , i, "value: ", next(zeroesOnesGen))

#test random_zeroes_ones
# startId = 0
# expectedNumberOfIterations = 100
# print("random_zeroes_ones:")
#
# zeroesOnesGen = random_zeroes_ones()
# for i in range(startId, expectedNumberOfIterations):
#     print("id of iteration: " , i, "value: ", next(zeroesOnesGen))

#test iter_zeroes_ones_minus_ones
startId = 0
expectedNumberOfIterations = 100
print("iter_zeroes_ones_minus_ones:")

zeroesOnesGen = iter_zeroes_ones_minus_ones()
for i in range(startId, expectedNumberOfIterations):
    print("id of iteration: " , i, "value: ", next(zeroesOnesGen))
