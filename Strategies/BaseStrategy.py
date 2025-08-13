from abc import ABC , abstractmethod
import pandas as pd

class BaseStrategy(ABC):
    
    '''
    An interface for each strategy
    '''
    def get_signal(self, candle:pd.Series):
        '''
        Determines the position for a given candle
        '''
        pass
    
    



