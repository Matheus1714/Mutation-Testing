import pytest
from src.bubble_sort import bubble_sort
from random import randint

def test_empty_list():
    assert bubble_sort([]) == []

def test_one_element_in_list():
    assert bubble_sort([1]) == [1]

def test_2_elements_ordered_in_list():
    assert bubble_sort([1, 2]) == [1, 2]

def test_2_elements_not_ordered_in_list():
    assert bubble_sort([2, 1]) == [1, 2]

def test_2_elements_not_ordered_in_list():
    assert bubble_sort([2, 1]) == [1, 2]

def test_n_elements_not_ordered_in_list():
    arr = [randint(0, 1000) for _ in range(100)]
    assert bubble_sort(arr) == sorted(arr)

def test_n_elements_negative_not_ordered_in_list():
    arr = [randint(-1000, 1000) for _ in range(100)]
    assert bubble_sort(arr) == sorted(arr)



