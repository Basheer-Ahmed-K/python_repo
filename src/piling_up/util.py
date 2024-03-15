import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")


def pillingUp():
    ans = ''
    t = int(input())
    for i in range(t):
        n = int(input())
        l = list(map(int, input().split()))
        b = []
        while len(l) > 0:
            if l[-1] > l[0]:
                b.append(l.pop(-1))
            else:
                b.append(l.pop(0))
        c = b.copy()
        b.sort(reverse=True)
        if b == c:
            ans += 'Yes\n'
        else:
            ans += 'No\n'
    logging.info(ans)
    return ans


if __name__ == '__main__':
    pillingUp()
