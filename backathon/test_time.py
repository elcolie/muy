from timeit import default_timer as timer

import requests


def test_time():
    start = timer()
    url = "http://comtrade.un.org/api/get?max=500&type=C&freq=M&px=HS&ps=201906&r=all&p=0&rg=all&cc=TOTAL"
    res = requests.get(url)
    end = timer()
    print(end - start)  #


def main():
    test_time()


if __name__ == '__main__':
    main()
