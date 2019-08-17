import requests
from tqdm import tqdm

from const import *


def download():
    """Async call"""

    for rg in tqdm(TRADE_REGIMES):  # 1 -> import
        for r in tqdm(COUNTRIES):  # 20 countries
            for cc in CC_THREE:  # 3 products
                print(f"{rg} {r} {cc}")
                for year in tqdm(range(2014, 2018 + 1)):  # 5 years
                    for month in tqdm(range(1, 12 + 1)):  # 12 months
                        url = f"http://comtrade.un.org/api/get"
                        payload = {
                            'max': 50000,
                            'type': 'C',
                            'freq': 'M',
                            'px': 'HS',
                            'ps': f"{year}{str(month).zfill(2)}",
                            'r': r,
                            'p': 0,
                            'rg': '1',
                            'cc': cc,
                            'fmt': 'csv',
                        }
                        res = requests.get(url, params=payload)
                        try:
                            assert 200 == res.status_code
                        except:
                            f = open(f"[error]_{rg}_{r}_{cc}_{year}_{month}.csv", 'wb')
                            f.write(res.text.encode('utf8'))
                            f.close()
                        f = open(f"{rg}_{r}_{cc}_{year}_{month}.csv", 'wb')
                        f.write(res.text.encode('utf8'))
                        f.close()
