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
        Code for executing an order. An order is a dictionary that contains the name, number of stocks requested, and 
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
        elif order['type'] =='borrow':
            self.borrow_and_sell(order['name'], order['number_of_stocks'])
            self.order_log.append(order)
            return True
        return False
    
    def borrow_and_sell(self , ticker, n_stocks):
        '''
        Borrows and sells n stocks in the case of a short. Saves loaned stocks in shorts dictionary.
        '''
        self.shorts['ticker'] = n_stocks
        self.portfolio.change_balance(self.portfolio.positions[ticker]['current_price'] * n_stocks) 
       

    def buy_stocks(self , ticker, n_stocks):
        '''
        Buys n stocks for a given ticker
        '''
        self.portfolio.update_n_stocks(ticker, n_stocks)
        self.portfolio.change_balance(-1 * self.portfolio.positions[ticker]['current_price'] * n_stocks)
    
    def sell_stocks(self, ticker, n_stocks):
        '''
        sells n stocks on a given ticker
        '''
        self.portfolio.update_n_stocks(-1 * n_stocks)
        self.portfolio.change_balance(self.portfolio.positions[ticker]['current_price'] * n_stocks)

    def log(self):
        '''
        Stores the updated order log in a store file upon request
        '''
        pd.DataFrame(self.order_log).to_csv(os.path.join('.', 'Store', 'OrderLog'))

    def get_comission(v_trade, rate=0.02) -> float:
        return v_trade * rate

    
   
        


        
 
        
