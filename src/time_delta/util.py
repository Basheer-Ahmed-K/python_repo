import logging


def time_delta(t1, t2):
    ans = ''
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    from datetime import datetime
    t1, t2 = map(lambda s: datetime.strptime(s, "%a %d %b %Y %H:%M:%S %z"), [t1, t2])
    ans += str(int(abs(t1 - t2).total_seconds()))
    logging.info(str(int(abs(t1 - t2).total_seconds())))
    # print(ans)
    return ans
