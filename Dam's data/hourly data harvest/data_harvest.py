import requests
import pandas as pd
import matplotlib.pyplot as plt
from requests.adapters import HTTPAdapter
from urllib3.util.ssl_ import create_urllib3_context
import ssl
from datetime import datetime, timedelta


class TLSAdapter(HTTPAdapter):
    def init_poolmanager(self, connections, maxsize, block=False, **pool_kwargs):
        ctx = create_urllib3_context(ciphers='DEFAULT@SECLEVEL=1')
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        pool_kwargs['ssl_context'] = ctx
        return super().init_poolmanager(connections, maxsize, block, **pool_kwargs)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'}

session = requests.Session()
session.mount('https://', TLSAdapter())

start_date = datetime.strptime('4/7/2022', '%m/%d/%Y')
end_date = datetime.strptime('3/26/2025', '%m/%d/%Y')
delta = timedelta(days=1)

all_dfs = []

current_date = start_date
while current_date <= end_date:
    date_str = f"{current_date.month}/{current_date.day}/{current_date.year}"
    url = f'https://www.nwd-wc.usace.army.mil/dd/nwdp/project_hourly/webexec/rep?r=bcl&date={date_str}'
    try:
        response = session.get(url, headers=headers, verify=False)
        tables = pd.read_html(response.text)
        df = tables[0]
        df['Date'] = current_date
        all_dfs.append(df)
    except Exception as e:
        print(f"Failed to process {date_str}: {e}")
    current_date += delta

final_df = pd.concat(all_dfs, ignore_index=True)
print(final_df.head())


numeric_cols = final_df.select_dtypes(include=['number']).columns
for col in numeric_cols:
    plt.figure(figsize=(12, 6))
    plt.plot(final_df['Date'], final_df[col])
    plt.title(f'{col} over Time')
    plt.xlabel('Date')
    plt.ylabel(col)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

print(final_df.head())
#precipitation
#Tmax and Tmin

