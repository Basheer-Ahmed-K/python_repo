import logging
import numpy


def linearAlgebra():
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    N = int(input())
    arr = []
    for _ in range(N):
        row = list(map(float, input().split()))
        arr.append(row)
    logging.info(round(numpy.linalg.det(arr), 2))
    return round(numpy.linalg.det(arr), 2)
