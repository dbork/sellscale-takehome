import { useState } from 'react';

import LoggedIn from './loggedIn.js'
import './App.css';

function App() {
    const [isLoggedIn, setLoggedIn] = useState(false);
    const [username, setUsername] = useState('');

    function handleLogin(e) {
        fetch(
            `http://127.0.0.1:5000/login/${username}`, {
                method: 'GET',
                credentials: 'include'
            }
        )
        setLoggedIn(true);
    }

    return (
        <div className="App">
            <header className="App-header">
                <p>
                    SellScaleHood
                </p>
                <div className="box">
                    { 
                        isLoggedIn ? 
                        <LoggedIn username={username}/> : 
                        <form onSubmit={handleLogin}>
                            <div className="login-flex">
                                please enter your username
                                <input className="login-input" onChange={
                                    e => setUsername(e.target.value)
                                }/>
                            </div>
                        </form>
                    }
                </div>
            </header>
        </div>
    );
}

export default App;
