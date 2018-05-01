import React, { Component } from 'react';
import { connect } from 'react-redux';
import { withRouter, Link }  from 'react-router-dom';
import logo from './logo.svg'

import './index.css';


class NavBar extends Component {

  navigate = (e) => {
    const activeLi = document.getElementsByClassName('Navbar-nav-li-active')[0];
    activeLi.classList.remove('Navbar-nav-li-active');
    e.currentTarget.classList.add('Navbar-nav-li-active');
  }

  render() {
    console.log('In da navbar!');
    return (
      <div className='NavBar-container'>
        <div className='NavBar-logo-container'>
          <img src={ logo } />
        </div>
        <div className='NavBar-navigation-container'>
          <div className='Navbar-nav'>
            <ul>
              <li className='Navbar-nav-li-active' onClick={ this.navigate }><Link to='/'>Home</Link></li>
              <li onClick={ this.navigate }><Link to='/'>Search</Link></li>
              <li onClick={ this.navigate }><Link to='/'>Profile</Link></li>
            </ul>
          </div>
          <div className='NavBar-auth-container'>
            <button className='NavBar-auth-signup'>Signup</button>
            <button className='NavBar-auth-login'>Login</button>
          </div>
        </div>
      </div>
    );
  }
}

const mapStateToProps = (state, props) => {
  return {

  }
}

export default withRouter(connect(mapStateToProps)(NavBar));