from statsmodels.tsa.arima.model import ARIMA
import pmdarima as pm

def arima_model(data, 
                n_diffs: int = 1,
                start_p: int = 0, max_p: int = 2,
                start_q: int = 0, max_q: int = 2,
                m: int = 1, 
                seasonal: bool = False,
                stepwise: bool = True,
                trace: bool = True,
):
    return pm.auto_arima(data, 
                start_p=start_p, max_p=max_p,
                start_q=start_q, max_q=max_q,
                m=m,
                seasonal=seasonal,
                stepwise=stepwise,
                trace=trace,
                error_action='ignore',
                suppress_warnings=True,
                n_diffs=n_diffs)
