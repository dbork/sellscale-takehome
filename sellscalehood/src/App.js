import { useState } from 'react';

import './App.css';

function App() {
    const [isLoggedIn, setLoggedIn] = useState(false);

    function handleLogin(e) {
        setLoggedIn(true);
    }

    return (
        <div className="App">
            <header className="App-header">
                <p>
                    SellScaleHood
                </p>
                <div className="white-box">
                    { 
                        isLoggedIn ? 
                        'login' : 
                        <form onSubmit={handleLogin}>
                            <div className="login-flex">
                                Please enter your username.
                                <input className="login-input" name='firstName'/>
                            </div>
                        </form>
                    }
                </div>
            </header>
        </div>
    );
}

export default App;
