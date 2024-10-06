from user import User

USER_ID = 0

# CLI implementation for debugging
def run():
    user = User(USER_ID)

    while True:
        print('Cash on hand: ${:.2f} USD'.format(user.cash))
        command = input("Enter command ('help' for usage): ").split()
            
        if command[0] == 'query':
            price, curr = user.query(command[1])
            print(
                'Current price of ticker {}: ${} {}'.format(
                    command[1].upper(), 
                    price,
                    curr
                )
            )

        if command[0] == 'buy':
            user.buy(command[1], int(command[2]))

        if command[0] == 'sell':
            user.sell(command[1], int(command[2]))

        if command[0] == 'view':
            for line in user.view_portfolio():
                print(
                    '{} stock{} of {}'.format(
                        line[2], 
                        's' if line[2] == 1 else 's',
                        line[1].upper()
                    )
                )

        if command[0] == 'help':
            print('''Usage:
                'query ticker': query a stock ticker
                'buy ticker amount': buy an amount of a stock
                'sell ticker amount': sell an amount of a stock
                'view': view portfolio 
                'quit': quit
                'help': print this message'''
            )

        if command[0] == 'quit':
            break
