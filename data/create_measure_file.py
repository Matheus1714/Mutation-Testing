from typing import List, Tuple
import os

def create_measure_file(file_path:str, measures: List[Tuple[float, float]]):
    with open(file_path, 'wb') as f:
        for measure in measures:
            mi, dmi = measure

            line = "{} {}\n".format(mi, dmi)

            f.write(line.encode('utf-8'))
