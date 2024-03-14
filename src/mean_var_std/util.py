import numpy as np
import logging


def MeanVarStd():
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    N, _ = map(int, input().split())
    array = np.array([input().split() for _ in range(N)], int)
    row_means = np.mean(array, axis=1)
    column_variances = np.var(array, axis=0)
    array_std = np.std(array)
    row_means_str = np.array2string(row_means, separator=' ')
    column_variances_str = np.array2string(column_variances, separator=' ')
    array_std_str = str(round(array_std, 11))
    logging.info(row_means_str + " " + column_variances_str + " " + array_std_str)
    return row_means_str + " " + column_variances_str + " " + array_std_str
