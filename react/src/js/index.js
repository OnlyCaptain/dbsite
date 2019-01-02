import React from 'react';
import ReactDOM from 'react-dom';
import MainPage from './components/root'
import WrappedNormalLoginForm from './components/login'

ReactDOM.render(<WrappedNormalLoginForm />, document.getElementById('mainContainer'));