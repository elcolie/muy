import time
from timeit import default_timer as timer

import requests

from backathon.const import TRADE_REGIMES, REPORTER_AREAS, COMMODITY_CODES


def download():
    """Async call"""

    for rg in TRADE_REGIMES:
        for r in REPORTER_AREAS:
            time.sleep(5)
            for cc in COMMODITY_CODES:
                start = timer()
                print(f"{rg} {r} {cc}")
                for year in range(2010, 2019 + 1):
                    for month in range(1, 12 + 1):
                        url = f"http://comtrade.un.org/api/get"
                        payload = {
                            'max': 50000,
                            'type': 'C',
                            'freq': 'M',
                            'px': 'HS',
                            'ps': f"{year}{str(month).zfill(2)}",
                        }
                        res = requests.get(url, params=payload)
                        assert 200 == res.status_code
                        f = open(f"{rg}_{r}_{cc}.csv", 'w')
                        f.write(res.text.encode('utf8'))
                        f.close()
                        end = timer()
                        print(end - start)
