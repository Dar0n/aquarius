import React, { Component } from 'react';
import { withRouter } from 'react-router-dom';
import { connect } from 'react-redux';
import { countries } from '../../store/constants';

import './index.css';

class NewRestaurant extends Component {

  constructor(props){
    super(props);

    this.state = {
      name: '',
      category: '',
      country: '',
      street: '',
      city: '',
      zip: '',
      website: '',
      phone: '',
      email: '',
      opening_hours: '',
      price_level: '',
      image: '',
    }
  }

  render() {
    return (
      <div className='NewRestaurant-container'>
        <form className='NewRestaurant-form' onSubmit={ this.handleLoginSubmit }>
          <h1>Create new restaurant</h1>
          <div className='NewRestaurant-formfields-container'>
            <fieldset>
              <legend>Basic</legend>
              <p>
                <label htmlFor=''>Name<abbr title="required">*</abbr></label>
                <input 
                  type='text' 
                  value={ this.state.name }
                  onChange={ this.handleNameChange }
                />
              </p>
              <p>
                <label htmlFor=''>Category<abbr title="required">*</abbr></label>
                <input 
                  type='text' 
                  value={ this.state.category }
                  onChange={ this.handleCategoryChange }
                />
              </p>
              <p>
                <label htmlFor=''>Country<abbr title="required">*</abbr></label>
                
                <select name='Country'>
                  {
                    Object.keys(countries).map(index => {
                      return <option value={ countries[index] }>{ countries[index] }</option>
                    })
                  }
                </select>
              </p>
            </fieldset>
            {/* <input 
              type='password' 
              placeholder='Password'
              value={ this.state.password }
              onChange={ this.handlePasswordChange } */}
            {/* /> */}
          </div>
          <button onClick={ this.handleValidationSubmit }>Login</button>
        </form>
      </div>
    )
  }
}

const mapStateToProps = (state, props) => {
  return {

  }
}

export default withRouter(connect(mapStateToProps)(NewRestaurant));