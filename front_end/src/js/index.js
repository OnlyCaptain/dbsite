import React from 'react';
import ReactDOM from 'react-dom';
import MainPage from './components/root'
import WrappedNormalLoginForm from './components/login'
import WrapperNormalRegisterForm from './components/register'
import {
    BrowserRouter as Router,
    Route,
    Switch
} from 'react-router-dom';

ReactDOM.render(
    <Router>
        <Switch>
            <Route exact path="/" component={WrappedNormalLoginForm} />
            <Route path="/login" component={WrappedNormalLoginForm} />
            <Route path="/register" component={WrapperNormalRegisterForm} />
            <Route path="/User/:id" component={MainPage} />
        </Switch>
    </Router>
    , document.getElementById('mainContainer')
);