# EXERCISE 12.1
#
# Write tests for the Vector class (Homework 6) using the 'unittest' or 'pytest' module.

from classes_6.homework.exercise_6_1 import Vector
import pytest
import math

@pytest.fixture   # decorator
def vectorA():
    return Vector(1, 2, 3)
@pytest.fixture
def vectorB():
    return Vector(1, 2, 4)

def test_init(vectorA):
    assert vectorA.x == 1
    assert vectorA.y == 2
    assert vectorA.z == 3

def test_repr(vectorA):
    assert str(vectorA) == "Vector(1, 2, 3)"

def test_eq(vectorA, vectorB):
    assert vectorA == vectorA
    assert not vectorA == vectorB

def test_neq(vectorA, vectorB):
    assert not vectorA != vectorA
    assert vectorA != vectorB

def test_add(vectorA, vectorB):
    assert vectorA + vectorB == Vector(2, 4, 7)

def test_sub(vectorA, vectorB):
    assert vectorB - vectorA == Vector(0, 0, 1)

def test_mul(vectorA, vectorB):
    assert vectorB * vectorA == 17

def test_cross(vectorA, vectorB):
    assert vectorA.cross(vectorB) == Vector(2, -1, 0)

def test_length(vectorA):
    assert vectorA.length() == math.sqrt(14)
def test_hash(vectorA, vectorB):
    assert not vectorA is vectorB
    assert vectorA is vectorA

def test_isParallel(vectorA, vectorB):
    assert not vectorA.isParallel(vectorB)
    assert  vectorA.isParallel(Vector(2,4,6))

def test_isZero(vectorA):
    assert not vectorA.isZero()
    assert Vector(0,0,0).isZero()

def test_getUnitVector(vectorA):
    assert vectorA.getUnitVector() == Vector(1/math.sqrt(14), 2/math.sqrt(14), 3/math.sqrt(14))

if __name__ == "__main__":
    pytest.main()

#python test_set.py