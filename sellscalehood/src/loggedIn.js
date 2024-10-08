import { useEffect, useState } from 'react'
import BuySellInterface from './buySellInterface.js'

import './loggedIn.css';

function LoggedIn({username}) {
    const [cash, setCash] = useState(0);
    const [ticker, setTicker] = useState('');
    const [portfolio, setPortfolio] = useState([]);
    const [price, setPrice] = useState(0);
    const [curr, setCurr] = useState('');

    useEffect(() => {
        fetch(
            `http://127.0.0.1:5000/get_cash/${username}`, {
                method: 'GET',
                credentials: 'include',
            }
        ).then(
            (res) => res.json()
        ).then(
            (data) => setCash(data.cash)
        )
    })

    useEffect(() => {
        fetch(
            `http://127.0.0.1:5000/view_portfolio/${username}`, {
                method: 'GET',
                credentials: 'include',
            }
        ).then(
            (res) => res.json()
        ).then(
            (data) => setPortfolio(data)
        )
    })

    function handleTicker(e) {
        e.preventDefault();
        fetch(
            `http://127.0.0.1:5000/get_price/${username}&${ticker}`, {
                method: 'GET',
                credentials: 'include',
            }
        ).then(
            (res) => res.json()
        ).then(
            (data) => {
                setPrice(data.price);
                setCurr(data.currencyCode);
            }
        )
    }

    function portToString(el) {
        return(`${el[2]} share${el[2] == 1 ? '' : 's'} of ${el[1]}`)
    }   

    return (
        <div className='logged-in'>
            <div className='cash-text'> 
                hello {username}. your cash on hand is ${cash}
            </div>
            <div className='horiz-flex'> 
                <div className='vert-flex'>
                    <div className='cash-text'>
                        enter a ticker
                    </div>
                    <form onSubmit={e => handleTicker(e)}>
                        <input className='ticker-input' onChange={
                            e => setTicker(e.target.value)
                        }/>
                    </form>
                    {
                        price ?
                        <BuySellInterface 
                            username={username}
                            ticker={ticker}
                            price={price}
                            curr={curr}
                        /> :
                        ''
                    }
                </div>
                <div className='black-box'>
                    <div className='portfolio-text'>
                        your portfolio
                    </div>
                    <div className='portfolio-text'>
                    {portfolio.map(el => portToString(el))}
                    </div>
                </div>
            </div>
        </div>
    )

}

export default LoggedIn;
