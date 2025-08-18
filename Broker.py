import pandas as pd 
from Portfolio import Portfolio
from DataProcessing import data_manager
import os

class Broker:
    def __init__(self, portfolio:Portfolio, processor:data_manager):
        self.portfolio = portfolio
        self.order_log = []
        self.processor = processor
        self.shorts = {} #dictionary storing the quantity of stocks borrowed. KEY: stock_name, VALUE: n_stocks
        

    def execute_order(self, order: dict):
        '''
        Code for executing an order
        '''
        if order == None: raise ValueError('order is None. Please input a proper, dictionary formatted, order.')
        #already existing order
        if order['type'] == 'buy':
            self.buy_stocks(order['name'] , order['number_of_stocks'], order['position'])
            self.order_log.append(order)
            return True
        elif order['type'] == 'sell':
            self.sell_stocks(order['name'], order['number_of_stocks'], order['position'])
            self.order_log.append(order)
            return True
        return False
        

    def buy_stocks(self , ticker, n_stocks, position):
        if position == 'SHORT':
            self.shorts['ticker'] = n_stocks
            self.portfolio.update_n_stocks(ticker , n_stocks) #
            return 
        self.portfolio.update_n_stocks(ticker, n_stocks)
        self.portfolio.change_balance(-1 * self.portfolio[ticker]['current_price'] * n_stocks)
    
    def sell_stocks(self, ticker, n_stocks, position):
        if position == 'SHORT':
            self.shorts.pop(ticker)
        self.portfolio.update_n_stocks(-1 * n_stocks)
        self.portfolio.change_balance(self.portfolio[ticker]['current_price'] * n_stocks)

    def log(self):
        '''
        Stores the updated order log in a store file upon request
        '''
        pd.DataFrame(self.order_log).to_csv(os.path.join('.', 'Store', 'OrderLog'))

   
        


        
 
        
