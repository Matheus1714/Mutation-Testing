from typing import List

def sum(arr:List[float])->float:

    acc = 0
    n = len(arr)
    for i in range(n):
        acc += arr[i]
    
    return acc