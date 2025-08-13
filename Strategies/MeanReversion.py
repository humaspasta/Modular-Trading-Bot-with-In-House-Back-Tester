from BaseStrategy import BaseStrategy
import pandas as pd

class mean_reversion(BaseStrategy):
    '''
    A python implimentation of the mean reversion strategy. 
    '''


    def __init__(self, lower= -0.03, upper=0.05):
        super().__init__()
        self.total_sum = 0.0
        self.total_n = 0
        self.mean = 0.0
        self.lower = lower
        self.upper = upper

    def calculate_candle_value(self, candle:pd.Series) -> float:
        '''
        determines the middle value of a given candle
        '''
        return (candle.loc['Close'] + candle.loc['Open']) / 2
    
    def calculate_price_deviation(self , p_candle:float) -> float:
        '''
        Returns the percent error as a decimal between the current candle price and the rolling mean.
        '''
        return (p_candle - self.mean) / self.mean
    
    def update_rolling_mean(self , candle:pd.Series) -> None:
        '''
        Updates the mean. Should be called by the backtester after each value is passed in.
        '''
        self.total_sum += self.calculate_candle_value(candle)
        self.total_n += 1
        self.mean = self.total_sum / self.total_n

    def get_signal(self, candle) -> str:
        '''
        Gets the signal
        '''
        price_dev = self.calculate_price_deviation(self.calculate_candle_value(candle))
        if self.total_n <= 10: return 'FLAT'
        else:
            if price_dev >= -0.05 and price_dev <= self.lower:
                return 'LONG'
            elif price_dev >= self.lower and price_dev <= self.upper:
                return 'FLAT'
            elif price_dev > self.upper:
                return 'SHORT'


    
