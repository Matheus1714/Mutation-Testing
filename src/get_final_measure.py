from typing import Tuple, List

from .sum import sum
from .bubble_sort import bubble_sort

def get_final_measure(data:Tuple[List, List])->Tuple[float, float]:
    
    s = sum(data[0])
    ds = sum(bubble_sort(data[1]))

    return s, ds