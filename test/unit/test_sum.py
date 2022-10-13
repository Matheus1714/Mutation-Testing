import pytest
from src.sum import sum
from random import randint
import math

def test_empty_list():
    assert sum([]) == 0

def test_one():
    value = randint(0, 10000)
    assert sum([value]) == value

