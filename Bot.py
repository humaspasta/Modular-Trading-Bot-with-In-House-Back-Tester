from Strategies import BaseStrategy
from Broker import Broker
from Portfolio import Portfolio
import statistics as stats
import pandas as pd

class bot:

    def __init__(self, strategies:list, broker: Broker, portfolio: Portfolio):
        self.strategies = strategies
        self.candle = None
        self.broker = broker
        self.portfolio = portfolio
    
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
        
    def get_current_price(self):
        self.candle['']


    def calc_position_size(self , ticker):
        pass

    
    def create_order(self, ticker_name) -> None:
        decision = self.calculate_decision()
        position_info = self.get_position_info(ticker_name)
        

        if position_info:
            if (position_info['position'] == 'LONG' or position_info['position'] =='SHORT') and decision == 'FLAT':

                order = {'name' : ticker_name,
                        'signal' : decision,
                        'number_of_stocks': position_info[ticker_name]['quantity'],
                        'type': 'sell'
                        } #selling all stocks to close position and return to flat
                result = self.broker.execute_order(order)

                if result:
                    self.portfolio.positions.pop(order['name'])
                
        else:
            if decision == 'LONG' or decision == 'SHORT':#in the first part of a long or short position, we always buy stocks.
                
                order = {'name' : ticker_name,
                        'signal' : decision,
                        'number_of_stocks': self.calc_position_size(ticker_name),
                        'type': 'buy'
                        }
                self.broker.execute_order(order)
                
                



    
    def get_position_info(self, ticker_name):
        return self.portfolio.positions[ticker_name]





            

 