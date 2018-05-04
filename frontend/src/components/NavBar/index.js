import React, { Component } from 'react';
import { connect } from 'react-redux';
import { withRouter, Link }  from 'react-router-dom';
import logo from './logo.svg'

import './index.css';

import Review from '../Review'


class NavBar extends Component {

  navigate = (e) => {
    const activeLi = document.getElementsByClassName('Navbar-nav-li-active')[0];
    activeLi.classList.remove('Navbar-nav-li-active');
    e.currentTarget.classList.add('Navbar-nav-li-active');
  }

  handleSignUp = (e) => {
    e.preventDefault();
    this.props.history.push('/signup');
  }

  render() {
    console.log('In da navbar!');
    return (
    
      <div className='NavBar-container'>
        <div className='NavBar-logo-container'>
          <img src={ logo } alt='Luna-logo'/>
          
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
            <button className='NavBar-auth-signup' onClick={ this.handleSignUp }>Signup</button>
            <button className='NavBar-auth-login'>Login</button>
            
          </div>
          
        </div>
        <Review />
      </div>
    );
  }
}

const mapStateToProps = (state, props) => {
  return {
    
  }
}

export default withRouter(connect(mapStateToProps)(NavBar));