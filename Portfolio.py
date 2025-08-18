from DataProcessing import data_manager

class Portfolio:

    def __init__(self, processor:data_manager):
        self.balance = 5000
        self.positions = {}
        self.equity = 5000
        self.processor = processor
        


    def parse_positions(self):
        rows = self.processor.cursor.fetchall()
        if rows == None: raise ValueError('table is none')
        for row in rows:
            self.positions[row[1]] =  {
                'signal': row[2],
                'quantity': row[3],
                'starting_price': row[4],
                'current_price': row[5]
            }
            

    def change_balance(self, amount) -> None:
        '''
        changes the balance by some amount. Put negative amount for spending
        '''
        self.balance += amount

    def add_position(self , ticker_name, signal, p_entry, n_stocks):
        '''
        Adds a position to the portfolio and sql database
        '''
        self.positions[ticker_name] = {
            'signal': signal,
            'quantity': n_stocks,
            'starting_price' : p_entry,
            'current_price' : 0
        }
        pass

    def update_n_stocks(self, name, n_stocks):
        '''
        Updates the number of stocks for a given stock
        '''
        pass

    def get_equity(self):
        return self.equity
    