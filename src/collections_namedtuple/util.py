import logging


def printAverage(total_students, table):
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    marks = [table._make(input().split()).MARKS for i in range(total_students)]
    logging.info(sum(map(int, marks)) / total_students)
    return sum(map(int, marks)) / total_students
