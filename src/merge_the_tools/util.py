import logging


def merge_the_tools(string, k):
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    ans = ''
    for i in range(0, len(string), k):
        substring = string[i: i + k]
        lst = list()
        for char in substring:
            if char not in lst:
                lst.append(char)
        for i in lst:
            ans+=i
        ans+='\n'
    logging.info(ans)
    return ans