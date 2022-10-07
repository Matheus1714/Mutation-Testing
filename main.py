from dotenv import dotenv_values

from mocks.create_measure_file import create_measure_file
from mocks.generate_measures import generate_measures

from src.get_data_file import get_data_file

if __name__ == '__main__':

    config = dotenv_values(".dev.env")

    file_path = config.get('DATA_FILE_PATH')
    quant_measure = int(config.get('QUANT_MEASURES'))
    measure_mean = float(config.get('MEASURE_MEAN'))
    measure_std = float(config.get('MEASURE_STD'))

    measures = generate_measures(quant_measure, measure_mean, measure_std)

    create_measure_file(file_path, measures)

    data = get_data_file(file_path)
    

