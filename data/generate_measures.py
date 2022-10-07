from typing import List, Tuple
from random import random, randint

def generate_measures(quant:int, mean:float, std:float)->List[Tuple[float, float]]:

    measures = []

    for _ in range(quant):
        
        signal = (-1) * randint(0, 1)
        mi = mean + signal * std
        dmi = std * random()

        measure = (mi, dmi)
        measures.append(measure)    

    return measures