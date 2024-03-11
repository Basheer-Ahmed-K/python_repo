def findPercentage(n):
    percentage = 0
    for i in n:
        percentage += i
    percentage = percentage / 3
    return "%.2f" % percentage
