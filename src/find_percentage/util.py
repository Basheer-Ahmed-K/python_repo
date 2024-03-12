import logging


def findPercentage():
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    student_name = student_marks[query_name]
    percentage = 0
    for i in student_name:
        percentage += i
    percentage = percentage / 3
    logging.info("%.2f" % percentage)
    return percentage

# def findPercentage(n):
#     percentage = 0
#     for i in n:
#         percentage += i
#     percentage = percentage / 3
#     return percentage
