from collections import namedtuple

from src.collections_namedtuple.util import printAverage

total_students = int(input())
table = namedtuple('studentInfo', input().split())
printAverage(total_students, table)