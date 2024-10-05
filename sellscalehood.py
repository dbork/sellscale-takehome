import yfinance as yf

import db_interface
import helper

# TODO: should all be in a user class with auth, probably
STARTING_CASH = 100000
USER_ID = 0
STOCKS_CONN = db_interface.open_conn()

conn = db_interface.open_conn()
try:
    db_interface.init_db(conn)
except:
    pass

def query(ticker): 
    info = yf.Ticker(ticker).info
    return info['currentPrice'], info['financialCurrency']

def buy(ticker, amt):
    pass

def sell(ticker, amt):
    pass

def view_portfolio():
    pass

# CLI implementation
if __name__ == "__main__":

    while True:
        command = input("Enter command ('help' for usage): ").split()
            
        if command[0] == 'query':
            price, curr = query(command[1])
            print(
                'Current price of ticker {}: ${} {}'.format(
                    command[1].upper(), 
                    price,
                    curr
                )
            )

        if command[0] == 'buy':
            buy(command[1], command[2])

        if command[0] == 'sell':
            sell(command[1], command[2])

        if command[0] == 'view':
            view_portfolio()

        if command[0] == 'help':
            print('''Usage:
                'query ticker': query a stock ticker
                'buy ticker amt': buy an amount of a stock
                'sell ticker amt': sell an amount of a stock
                'view': view portfolio 
                'quit': quit
                'help': print this message'''
            )

        if command[0] == 'quit':
            break
