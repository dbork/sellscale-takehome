import sqlite3

# Spin up databases if they don't exist
def init_db(conn):
   create_stocks = '''
        CREATE TABLE stocks (
            user_id INT,
            ticker TEXT,
            amount INT
        );
   '''
   create_users = '''
        CREATE TABLE users (
            user_id INT,
            username TEXT,
            cash FLOAT
        )
   '''
   conn.execute(create_stocks)
   conn.execute(create_users)
   conn.commit()

# Connect to the database, returning conn object
def open_conn():
    conn = sqlite3.connect('db/sellscalehood.db')

    try:
        init_db(conn)
    except:
        pass

    return conn

# Close connection to the database
def close_conn(conn):
    conn.close()

# Insert row into the stocks table
def insert_stocks(conn, user_id, ticker, amount):
    query = 'INSERT INTO stocks ({}) VALUES ({});'.format(
        'user_id, ticker, amount', 
        ', '.join(
            [
                str(user_id),
                "'{}'".format(ticker),
                str(amount)
            ]
        )
    )

    # Note that we reopen a cursor for each db operation; this is extra work, 
    # but it saves us from having to think about and pass a cursor object back
    # and forth in addition to the conn object
    cursor = conn.cursor()
    cursor.execute(query)

    # We also commit after every db operation, to save data in the event of
    # premature termination of a session
    conn.commit()

# Update row in the stocks table
def update_stocks(conn, user_id, ticker, amount):
    if amount == 0:
        delete_stocks(conn, user_id, ticker)
    else:
        query = '''
            UPDATE stocks 
            SET amount = {} 
            WHERE user_id = {} AND ticker = '{}'
        '''.format(amount, user_id, ticker)
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()

# Delete row from the stocks table
def delete_stocks(conn, user_id, ticker):
    query = '''
        DELETE FROM stocks 
        WHERE user_id = {} AND ticker = '{}'
    '''.format(user_id, ticker)
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()

# Get stocks with given ticker owned by a user
def get_stocks(conn, user_id, ticker):
    query = '''
        SELECT * FROM stocks WHERE user_id = {} AND ticker = '{}'
    '''.format(
        user_id,
        ticker
    )
    return conn.execute(query).fetchall()

# Get all stocks owned by a user
def get_all_stocks(conn, user_id):
    query = '''
        SELECT * FROM stocks WHERE user_id = {}
    '''.format(
        user_id
    )
    return conn.execute(query).fetchall()

# Create a new user in the user table
def insert_user(conn, user_id, username, cash):
    query = 'INSERT INTO users ({}) VALUES ({});'.format(
        'user_id, username, cash', 
        ', '.join(
            [
                str(user_id),
                "'{}'".format(username),
                str(cash)
            ]
        )
    )
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()

# Update the cash owned by an existing user
def update_user(conn, user_id, cash):
    query = '''
        UPDATE users 
        SET cash = {} 
        WHERE user_id = {}
    '''.format(cash, user_id)
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()

# Get user with given username
def get_user(conn, username):
    query = '''
        SELECT * FROM users WHERE username = '{}'
    '''.format(
        username
    )
    return conn.execute(query).fetchall()

# Get all users
def get_all_users(conn):
    query = '''
        SELECT * FROM users
    '''
    return conn.execute(query).fetchall()
