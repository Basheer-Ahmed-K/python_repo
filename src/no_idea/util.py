import logging


def noIdea():
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    n, m = (input().split())
    arr = list((input().split()))
    A = set(input().split())
    B = set(input().split())
    happiness = 0
    for x in arr:
        if x in A:
            happiness += 1
        elif x in B:
            happiness -= 1
    logging.info(happiness)
    return happiness
