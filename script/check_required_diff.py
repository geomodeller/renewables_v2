
import pandas as pd 
from pmdarima.arima import ndiffs, nsdiffs

def check_required_differencing(df: pd.DataFrame, col: str = 'primary'):
    print('------- Differencing required for stationarity (trend)-------'.center(50))
    for method in ['adf','kpss','pp']:
        print(f'Differencing required ({method}): {ndiffs(df[col], test = method)}')

    print('------- Differencing required for stationarity (seasonality) -------'.center(50))
    for method in ['OCSB','CH']:
        print(f'Differencing required for seasonality ({method}): {nsdiffs(df[col], m=15, test = method.lower())}')
