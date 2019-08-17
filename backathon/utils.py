import time
from tqdm import tqdm

from timeit import default_timer as timer

import requests

from const import *


def download():
    """Async call"""

    for rg in tqdm(TRADE_REGIMES):  # 4 types
        for r in tqdm(REPORTER_AREAS):  # 180 countries
            for cc in CC_SUGAR:  # 15
                start = timer()
                print(f"{rg} {r['id']} {cc}")
                for year in tqdm(range(2010, 2019 + 1)):  # 10 years
                    for month in tqdm(range(1, 12 + 1)):  # 12 months
                        url = f"http://comtrade.un.org/api/get"
                        payload = {
                            'max': 50000,
                            'type': 'C',
                            'freq': 'M',
                            'px': 'HS',
                            'ps': f"{year}{str(month).zfill(2)}",
                            'r': str(r['id']),
                            'p': 0,
                            'rg': rg,
                            'cc': cc,
                            'fmt': 'csv',
                        }
                        res = requests.get(url, params=payload)
                        try:
                            assert 200 == res.status_code
                        except:
                            print(f"{rg}_{r['id']}_{cc}_{year}_{month}.csv")
                        f = open(f"{rg}_{r['id']}_{cc}_{year}_{month}.csv", 'wb')
                        f.write(res.text.encode('utf8'))
                        f.close()
                        end = timer()
                        print(end - start)

