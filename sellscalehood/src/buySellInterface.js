import { useEffect, useState } from 'react'

import './buySellInterface.css';

function BuySellInterface({username, ticker, price, curr}) {

    function handleBuy(e) {
        fetch(
            `http://127.0.0.1:5000/buy/${username}&${ticker}&1`, {
                method: 'POST',
                credentials: 'include'
            }
        )
    }

    function handleSell(e) {
        fetch(
            `http://127.0.0.1:5000/sell/${username}&${ticker}&1`, {
                method: 'POST',
                credentials: 'include'
            }
        )
    }

    return (
        <div>
            {`price of ${ticker}: $${price} ${curr}`}
            <div className='horiz-flex'>
                <button type="button" onClick={handleBuy}>+</button>
                <button type="button" onClick={handleSell}>-</button>
            </div>
        </div>
    )
}

export default BuySellInterface;
