import logging


def print_formatted(number):
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    ans = ''
    width = len(bin(number)[2:])
    for i in range(1, number + 1):
        logging.info('{} {} {} {}'.format(str(i).rjust(width), oct(i)[2:].rjust(width), hex(i)[2:].upper().rjust(width), bin(i)[2:].rjust(width)))
        ans += '{} {} {} {}\n'.format(str(i).rjust(width), oct(i)[2:].rjust(width), hex(i)[2:].upper().rjust(width), bin(i)[2:].rjust(width))
    return ans
