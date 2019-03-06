import React from 'react';
import { Route } from 'react-router-dom'
import { Grid } from 'semantic-ui-react';

import { HomeView, LoginView, SignUpView, NavBar } from '../modules';

const App = () => {
    return (
        <div>
            <NavBar/>
                <div>
                    <Route path='/' exact component={HomeView} />
                    <Route path='/login' exact component={LoginView} />
                    <Route path='/signup' exact component={SignUpView} />
                </div>
        </div>
    );
};

export default App;