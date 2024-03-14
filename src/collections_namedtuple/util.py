import logging
from collections import namedtuple


def printAverage():
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    total_students = int(input())
    table = namedtuple('studentInfo', input().split())
    marks = [table._make(input().split()).MARKS for i in range(total_students)]
    logging.info(sum(map(int, marks)) / total_students)
    return sum(map(int, marks)) / total_students
