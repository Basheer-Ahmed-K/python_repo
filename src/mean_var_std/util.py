import numpy as np


def MeanVarStd():
    N, _ = map(int, input().split())
    x = np.array([input().split() for _ in range(N)], int)
    print(np.mean(x, axis=1), np.var(x, axis=0), round(np.std(x), 11), sep='\n')
    return np.mean(x, axis=1), np.var(x, axis=0), round(np.std(x), 11)
