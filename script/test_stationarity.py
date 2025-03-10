from statsmodels.tsa.stattools import kpss, adfuller
import pandas as pd
import numpy as np
def test_stationarity(timeseries: pd.Series | np.ndarray, test_method: str):
    """
    Run a stationarity test on the given timeseries and print the results.

    Parameters
    ----------
    timeseries : array-like
        The time series to test for stationarity.
    test_method : str
        The name of the stationarity test to run. Options are 'kpss' or 'adfuller'.
    """
    
    if test_method.lower() == 'kpss':
        result = kpss(timeseries)
        items = result[3].items()
    elif test_method.lower() in ['adfuller', 'adf']:
        result = adfuller(timeseries)
        items = result[4].items()

    print(f'Test: {test_method}')
    print('Test Statistic: %.4f' % result[0])
    print('p-value: %.4f' % result[1])
    print('Critical Values:')
    for key, value in items:
        print('\t%s: %.3f' % (key, value))
    print()
