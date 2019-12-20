"""
Answer: Year ~5 thousand
"""
import calendar

import arrow


def press(start_dt):
    while True:
        start_dt = start_dt.shift(years=1)
        print(start_dt)
        if calendar.isleap(start_dt.year) and (start_dt.month == 2) and (start_dt.day == 29):
            print("Answer")
            return start_dt
        if start_dt.isoweekday() == 2:
            print("Go back 2 days")
            start_dt = start_dt.shift(days=-2)


def main():
    """
    If it's February 29th (in a leap year), pressing the red button makes the time machine explode
    If it's a Tuesday, pressing the red button makes the time machine go backwards 2 days into the past
    If i keep pressing the red button, in what year will I be when the time machine explodes?
    :return:
    """
    # "Saturday 14 December 2019"
    start_dt = arrow.get(2019, 12, 14)

    # Start press button
    print(press(start_dt))


if __name__ == '__main__':
    main()
