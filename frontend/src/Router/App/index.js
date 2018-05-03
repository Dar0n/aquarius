import React, { Component } from 'react';
import './index.css';
import { connect } from 'react-redux';
import { withRouter } from 'react-router-dom';

class App extends Component {
  render() {
    console.log(this.props);
    return (
      <div></div>
    );
  }
}


const mapStateToProps = (state) => {
  return {
    tokens: state.tokens,
    loginStatus: state.loginStatus.loginStatus,
  }
}

export default withRouter(connect(mapStateToProps)(App));