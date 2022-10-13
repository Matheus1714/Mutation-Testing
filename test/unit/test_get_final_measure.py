import pytest
from src.get_final_measure import get_final_measure
from random import randint, random

def test_common_example_data():
    data = [
        [randint(19, 21) for _ in range(100)],
        [random() for _ in range(100)]
    ]
    assert get_final_measure(data) == (sum(data[0]), sum(data[1]))

def test_empty_data():
    data = [
        [],
        []
    ]
    assert get_final_measure(data) == (0, 0)