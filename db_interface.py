import sqlite3

# Spin up databases if they don't exist
def init_db(conn):
   query = '''
        CREATE TABLE stocks (
            user_id INT,
            ticker TEXT,
            amount INT
        )
   '''
   conn.execute(query)
   conn.commit()

# Connect to the database, returning conn object
def open_conn():
    conn = sqlite3.connect('db/stocks.db')
    return conn

# Close connection to the database
def close_conn(conn):
    conn.close()

# Insert row into the database
def insert(conn, user_id, ticker, amount):
    query = 'INSERT INTO stocks ({}) VALUES ({});'.format(
        'user_id, ticker, amount', 
        ', '.join(
            user_id,
            ticker,
            amount
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

# Update row in the database
def update(conn):
    conn.commit()
    pass

# Delete row from the database
def delete(conn):
    conn.commit()
    pass

# Get stocks with given ticker owned by a user
def get(conn, user_id, ticker):
    pass

# Get all stocks owned by a user
def get_all(conn, user_id):
    pass
