'''
Link to exe: https://exercism.org/tracks/python/exercises/gigasecond
Materials: https://bobbyhadz.com/blog/python-add-seconds-to-datetime
Documentation: https://docs.python.org/3/library/datetime.html
'''
from datetime import datetime, timedelta

def add(moment):
    return moment + timedelta(seconds=1000000000)
