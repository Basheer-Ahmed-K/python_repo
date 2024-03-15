from collections import Counter
import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")


def wordOrder():
    ans = []
    n = int(input())
    ls = []
    for _ in range(n):
        ls.append(input())
    dic = Counter(ls)
    ans.append(str(len(dic.keys())))
    ans.append(list(dic.values()))
    logging.info(ans)
    return str(ans)
