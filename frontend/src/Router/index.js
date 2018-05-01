import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import App from './App';
import ScrollToTop from '../components/ScrollToTop';
import ApplicationBar from '../components/ApplicationBar';

const Home = (props) => {
    return (
      <Router>
        <Switch>
          <ScrollToTop>
            {/* <NavBar /> */}
            <Route exact path="/login" component={ App } />
          </ScrollToTop>
        </Switch>
      </Router>
    )
}


export default Home;