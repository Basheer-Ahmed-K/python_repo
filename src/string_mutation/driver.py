# from util import * # import all from utils file
from util import mutate_string # import specific func/method
import logging


s = input("Enter the string: ")
i, c = input().split()
s_new = mutate_string(s, int(i), c)
logging.warning(s_new)

