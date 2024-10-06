import yfinance as yf

import db_interface
import helper

STARTING_CASH = 100000

# TODO: auth, persist user cash
# TODO: pandas
class User:
    def __init__(self, user_id):
        self.user_id = user_id
        self.cash = STARTING_CASH
        self.conn = db_interface.open_conn()

    def query(self, ticker): 
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

        row = db_interface.get(self.conn, self.user_id, ticker)
        if row:
            new_amount = amount + row[0][2]
            db_interface.update(self.conn, self.user_id, ticker, new_amount)
        else:
            db_interface.insert(self.conn, self.user_id, ticker, amount)

        self.cash -= cost

    def sell(self, ticker, amount):

        price, curr = self.query(ticker)
        price_usd = helper.to_usd(price, curr)
        revenue = price_usd * amount

        # Throw an error if the user doesn't own enough of this stock
        row = db_interface.get(self.conn, self.user_id, ticker)
        if row:
            new_amount = row[0][2] - amount
            if new_amount < 0:
                raise Exception(
                    'You do not own enough of this stock for this transaction'
                )

            if new_amount == 0:
                db_interface.delete(
                    self.conn, 
                    self.user_id, 
                    ticker
                )

            else:
                db_interface.update(
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
        return db_interface.get_all(self.conn, self.user_id)

