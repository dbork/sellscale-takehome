import yfinance as yf

import db_interface
import helper

STARTING_CASH = 100000

class User:
    def __init__(self, username):
        self.conn = db_interface.open_conn()

        # Look for an existing user in the db
        existing_user = db_interface.get_user(self.conn, username)
        if row:
            self.user_id = row[0]
            self.cash = row[2]

        # If not found, create a new user with default starting cash
        else:
            self.user_id = len(db_interface.get_all_users())
            db_interface.insert_user(
                self.conn, 
                self.user_id, 
                username, 
                DEFAULT_CASH
            )
            self.username = username
            self.cash = DEFAULT_CASH

    def get_price(self, ticker): 
        info = yf.Ticker(ticker).info
        return info['currentPrice'], info['financialCurrency']

    def buy(self, ticker, amount):
        # Sanity check to make sure the user can afford this
        price, curr = self.query(ticker)
        price_usd = helper.to_usd(price, curr)
        cost = price_usd * amount
        if cost > self.cash:
            raise Exception(
                'You do not have enough money for this transaction.'
            )

        row = db_interface.get_stocks(self.conn, self.user_id, ticker)
        if row:
            new_amount = amount + row[0][2]
            db_interface.update_stocks(
                self.conn, 
                self.user_id, 
                ticker, 
                new_amount
            )
        else:
            db_interface.insert_stocks(
                self.conn, 
                self.user_id, 
                ticker, 
                amount
            )

        self.cash -= cost

    def sell(self, ticker, amount):

        price, curr = self.query(ticker)
        price_usd = helper.to_usd(price, curr)
        revenue = price_usd * amount

        # Throw an error if the user doesn't own enough of this stock
        row = db_interface.get_stocks(self.conn, self.user_id, ticker)
        if row:
            new_amount = row[0][2] - amount
            if new_amount < 0:
                raise Exception(
                    'You do not own enough of this stock for this transaction'
                )

            db_interface.update_stocks(
                self.conn, 
                self.user_id, 
                ticker, 
                new_amount
            )

        else:
            raise Exception(
                'You do not own enough of this stock for this transaction'
            )

        self.cash += revenue

    def view_portfolio(self):
        return db_interface.get_all_stocks(self.conn, self.user_id)

