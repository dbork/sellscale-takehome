

def to_usd(price, curr):
    if curr != 'USD':
        raise NotImplementedError(
            'Support for non-USD currencies not yet implemented.'
        )
