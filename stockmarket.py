"""
stockmarket 60 days and find the best and worst trade day

"""
from datetime import datetime

import arrow

class Record:
    def __init__(self, dt: str, value:float):
        pass

def main():
    with open('sp500.txt', 'r') as input:
        lines = input.readlines()
        arrow.get(datetime(2013, 5, 5), 'US/Pacific')
    return

if __name__ == '__main__':
    main()