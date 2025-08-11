from abc import ABC , abstractmethod

class BaseStrategy(ABC):
    
    '''
    An interface for each strategy
    '''
    def get_signal(self):
        '''
        Determines the position for a given candle
        '''
        pass
    
    



