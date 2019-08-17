import time
from timeit import default_timer as timer

import requests

from backathon.const import *


def download():
    """Async call"""

    for rg in TRADE_REGIMES:  # 4 types
        for r in REPORTER_AREAS:  # 180 countries
            time.sleep(5)
            for cc in CC_SUGAR:  # commodity codes
                start = timer()
                print(f"{rg} {r['id']} {cc}")
                for year in range(2010, 2019 + 1):  # 10 years
                    for month in range(1, 12 + 1):  # 12 months
                        url = f"http://comtrade.un.org/api/get"
                        payload = {
                            'max': 50000,
                            'type': 'C',
                            'freq': 'M',
                            'px': 'HS',
                            'ps': f"{year}{str(month).zfill(2)}",
                            'r': str(r),
                            'p': 0,
                            'rg': rg,
                            'cc': cc,
                            'fmt': 'csv',
                        }
                        res = requests.get(url, params=payload)
                        assert 200 == res.status_code
                        f = open(f"{rg}_{r}_{cc}.csv", 'w')
                        f.write(res.text.encode('utf8'))
                        f.close()
                        end = timer()
                        print(end - start)
