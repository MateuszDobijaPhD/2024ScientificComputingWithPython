# EXERCISE 5.3
#
# Create the generator random_walk(start) for a 1D random walker. If a position at a certain moment is x, then the next position can be x+1 or x-1 with equal probabilities. Find the final position after 100 moves (start=0). Repeat experiments.

import random
def random_walk(start):
    position = start
    availableSteps = [-1, 1]
    while True:
        selectedStep = random.choice(availableSteps)
        position += selectedStep
        yield position

#test
startPosition = 0
startIdOfMove = 0
expectedNumberOfMoves = 100
print("test of 1D random walker for startPosition =", startPosition, "\n")

randomWalkerGen = random_walk(startPosition)
for i in range(startIdOfMove, expectedNumberOfMoves):
    position = next(randomWalkerGen)
    print("id of performed move:", i, ", position after move:", position)


