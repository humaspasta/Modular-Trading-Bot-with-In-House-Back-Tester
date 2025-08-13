from Strategies import BaseStrategy
import statistics as stats
import pandas as pd

class bot:

    def __init__(self, strategies:list):
        self.strategies = strategies
        self.candle = None
    
    def next(self, new_candle:pd.Series):
        self.candle = new_candle

    def calculate_decision(self):
        '''
        Calculates the decision based on the highest frequency signal present amongst all signals
        '''
        if self.candle == None: raise ValueError('Candle was not initalized.')
        decisions = []
        for strategy in self.strategies:
            if not isinstance(strategy, BaseStrategy):
                raise ValueError(f'{strategy} not of type strategy')
            else:
                signal = strategy.get_signal(self.candle)
                decisions.append(signal)
        
        try: #in case of ties
            return stats.mode(decisions)
        except stats.StatisticsError:
            return 'FLAT'

    def act_on_signal(self, signal):
        #will code once the broker is finished
        pass