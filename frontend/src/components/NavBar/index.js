import React, { Component } from 'react';
import { connect } from 'react-redux';
import { withRouter } from 'react-router-dom';

class NavBar extends Component {
  render() {
    return (
      <div></div>
    );
  }
}

const mapStateToProps = (state, props) => {
  return {

  }
}

export default withRouter(connect(mapStateToProps)(ApplicationBar));