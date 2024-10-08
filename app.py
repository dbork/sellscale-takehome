from flask import Flask
from flask_cors import CORS

from constants import SECRET_KEY
from user import User

app = Flask(__name__)
CORS(app, supports_credentials=True)
app.secret_key = SECRET_KEY

@app.route('/get_price/<username>&<ticker>', methods=['GET'])
def get_price(username, ticker):
    data = User(username).get_price(ticker)
    return(
        {
            'price': data[0],
            'currencyCode': data[1]
        }
    )

@app.route('/buy/<username>&<ticker>&<amount>', methods=['POST'])
def buy(username, ticker, amount):
    try:
        data = User(username).buy(ticker, int(amount))
        return {'response': True}
    except Exception:
        return {'response': False}

@app.route('/sell/<username>&<ticker>&<amount>', methods=['POST'])
def sell(username, ticker, amount):
    try:
        data = User(username).sell(ticker, int(amount))
        return {'response': True}
    except Exception:
        return {'response': False}

@app.route('/view_portfolio/<username>', methods=['GET'])
def view_portfolio(username):
    data = User(username).view_portfolio()
    return data

@app.route('/login/<username>', methods=['GET'])
def login(username):
    return {'response': True}

@app.route('/get_cash/<username>', methods=['GET'])
def get_cash(username):
    return {'cash': User(username).get_cash()}
