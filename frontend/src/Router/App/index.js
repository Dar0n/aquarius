import React, { Component } from 'react';
import './index.css';
import { connect } from 'react-redux';
import { withRouter } from 'react-router-dom';
// import Card from '../../components/Restaurant'

class App extends Component {
  render() {
    console.log(this.props);
    return (
      <div>
        {/*<Card />*/}
      </div>
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