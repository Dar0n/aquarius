import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import App from './App';
import Signup from './Signup';
import ScrollToTop from '../components/ScrollToTop';
import NavBar from '../components/NavBar';
import Footer from '../components/Footer';

const Home = (props) => {
    return (
      <Router>
        <Switch>
          <ScrollToTop>
            <NavBar />
            <Route exact path="/" component={ App } />
            <Route exact path="/signup" component={ Signup } />
            {/* <Route exact path="/restaurant/:id" component={ Restaurant } /> */}

            <Footer />
          </ScrollToTop>
        </Switch>
      </Router>
    )
}


export default Home;