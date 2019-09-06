import pandas

from utils.logger import custom_logger

log = custom_logger()


def parse_json(file, col_arr):
    tuples = None
    try:
        df = pandas.read_json(file)
        subset = df[col_arr]
        tuples = [tuple(x) for x in subset.values]
    except Exception as e:
        log.error("Exception occurred while parsing json test input file {}."
                  "Error is {}".format(file, e))
    return tuples
