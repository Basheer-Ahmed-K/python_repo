import numpy, logging


def MinMax():
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    N, M = map(int, input().split())
    rows = []
    for _ in range(N):
        row = list(map(int, input().split()))
        rows.append(row)
    arr = numpy.array(rows)
    max_of_min = numpy.max(numpy.min(arr, axis=1))
    logging.info(max_of_min)
    return max_of_min
