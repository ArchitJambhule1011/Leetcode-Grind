"""

Write a program to count the number of days between two dates.

The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples.

"""

from datetime import datetime

class Solution:
    def daysbetweendates(self, day1:str, day2:str) -> int:
        dates = [day1, day2]
        dates = [datetime.strptime(date, "%Y-%m-%d") for date in dates]
        diff = max(dates) - min(dates)
        return diff.days