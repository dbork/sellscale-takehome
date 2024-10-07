from flask import Flask, session

from constants import SECRET_KEY
from user import User

app = Flask(__name__)
app.secret_key = SECRET_KEY

@app.route('/get_price/<ticker>', methods=['GET'])
def get_price(ticker):
    data = User(session['user_id']).get_price(ticker)
    return(
        {
            'price': data[0],
            'currencyCode': data[1]
        }
    )

@app.route('/buy/<ticker>&<amount>', methods=['POST'])
def buy(ticker, amount):
    try:
        data = User(session['user_id']).buy(ticker, amount)
        return {'response': True}
    except Exception:
        return {'response': False}

@app.route('/sell/<ticker>&<amount>', methods=['POST'])
def sell(ticker, amount):
    try:
        data = User(session['user_id']).sell(ticker, amount)
        return {'response': True}
    except Exception:
        return {'response': False}

@app.route('/view_portfolio', methods=['GET'])
def query():
    data = User(session['user_id']).view_portfolio()
    return data

@app.route('/login/<user_id>', methods=['GET'])
def login(user_id):
    session['user_id'] = user_id
    return {'response': True}

