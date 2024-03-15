import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')


def fun(s):
    import re
    return bool(re.fullmatch("[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{,3}", s))


def filter_mail(emails):
    return list(filter(fun, emails))


def ValidEmail():
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    logging.info(filtered_emails)
    return filtered_emails
