import calendar
import logging


def printDay(date, month, year):
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    ans = calendar.weekday(int(year), int(month), int(date))
    days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
    logging.info(days[ans])
    return days[ans]