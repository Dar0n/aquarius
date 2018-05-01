import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import App from './App';
import ScrollToTop from '../components/ScrollToTop';
import NavBar from '../components/NavBar';

const Home = (props) => {
    return (
      <Router>
        <Switch>
          <ScrollToTop>
            <NavBar />
            <Route exact path="/" component={ App } />
          </ScrollToTop>
        </Switch>
      </Router>
    )
}


export default Home;