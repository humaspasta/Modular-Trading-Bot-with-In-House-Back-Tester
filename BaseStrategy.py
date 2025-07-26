from abc import ABC , abstractmethod

class BaseStrategy(ABC):
    
    '''
    An interface for each strategy
    '''
    @abstractmethod
    def _init__(self, threshold, total_money=0, num_shares=0):
        self.states = ['SHORT', 'FLAT', 'LONG']
        self.total_money = total_money
        self.num_shares = num_shares

    @abstractmethod
    def determine_position(self):
        '''
        Determines the position for a given candle
        '''
        pass
    
    



