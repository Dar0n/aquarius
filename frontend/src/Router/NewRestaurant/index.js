import React, { Component } from 'react';
import { withRouter } from 'react-router-dom';
import { connect } from 'react-redux';
import { countries } from '../../store/constants';
import './index.css';

var rand = require("random-key");



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
            <div className='NewRestaurant-formfields-fieldset'>
              <legend>Basic</legend>
              <div className='NewRestaurant-formfields-fieldset-inputs'>
                <div>
                  <label htmlFor='name'>Name<abbr title="required">*</abbr></label>
                  <input 
                    id='name'
                    type='text' 
                    value={ this.state.name }
                    onChange={ this.handleNameChange }
                  />
                </div>
                <div>
                  <label htmlFor='category'>Category<abbr title="required">*</abbr></label>
                  <select name='Country' id='category'>
                    {
                      Object.keys(this.props.categories).map(index => {
                        return <option key={ rand.generate(10) } value={ this.props.categories[index] }>{ this.props.categories[index] }</option>
                      })
                    }
                  </select>
                </div>
                <div>
                  <label htmlFor='country'>Country<abbr title="required">*</abbr></label>
                  <select name='Country' id='country'>
                    {
                      Object.keys(countries).map(index => {
                        return <option key={ rand.generate(10) } value={ countries[index] }>{ countries[index] }</option>
                      })
                    }
                  </select>
                </div>
              </div>
            </div>
            <div className='NewRestaurant-formfields-fieldset'>
            <legend>Address</legend>
            <div className='NewRestaurant-formfields-fieldset-inputs'>
              <div>
                <label htmlFor='street'>Street<abbr title="required">*</abbr></label>
                <input 
                  id='street'
                  type='text' 
                  value={ this.state.street }
                  onChange={ this.handleStreetChange }
                />
              </div>
              <div>
                <label htmlFor='city'>City<abbr title="required">*</abbr></label>
                <input 
                  id='city'
                  type='text' 
                  value={ this.state.city }
                  onChange={ this.handleCityChange }
                />
              </div>
              <div>
                <label htmlFor='zip'>Zip<abbr title="required">*</abbr></label>
                <input 
                  id='zip'
                  type='text' 
                  value={ this.state.zip }
                  onChange={ this.handleZipChange }
                />
              </div>
              </div>
            </div>
            <div className='NewRestaurant-formfields-fieldset'>
            <legend>Contact</legend>
            <div className='NewRestaurant-formfields-fieldset-inputs'>
              <div>
                <label htmlFor='website'>Website<abbr title="required">*</abbr></label>
                <input 
                  id='website'
                  type='text' 
                  value={ this.state.website }
                  onChange={ this.handleWebsiteChange }
                />
              </div>
              <div>
                <label htmlFor='Phone'>Phone<abbr title="required">*</abbr></label>
                <input 
                  id='phone'
                  type='text' 
                  value={ this.state.phone }
                  onChange={ this.handlePhoneChange }
                />
              </div>
              <div>
                <label htmlFor='email'>Email<abbr title="required">*</abbr></label>
                <input 
                  id='email'
                  type='text' 
                  value={ this.state.email }
                  onChange={ this.handleEmailChange }
                />
              </div>
              </div>
            </div>
            <div className='NewRestaurant-formfields-fieldset'>
            <legend>Details</legend>
            <div className='NewRestaurant-formfields-fieldset-inputs'>
              <div>
                <label htmlFor='opening_hours'>Opening hours<abbr title="required">*</abbr></label>
                <input 
                  id='opening_hours'
                  type='text' 
                  value={ this.state.opening_hours }
                  onChange={ this.handleOpeningHoursChange }
                />
              </div>
              <div>
                <label htmlFor='Price_level'>Price level<abbr title="required">*</abbr></label>
                <input 
                  id='price_level'
                  type='text' 
                  value={ this.state.price_level }
                  onChange={ this.handlePriceLevelChange }
                />
              </div>
              <div>
                <label htmlFor='image'>Image<abbr title="required">*</abbr></label>
                <input type="file" id="file" name="file" multiple />
              </div>
              </div>
            </div>
            {/* <input 
              type='password' 
              placeholder='Password'
              value={ this.state.password }
              onChange={ this.handlePasswordChange } */}
            {/* /> */}
          </div>
          <button onClick={ this.handleValidationSubmit }>Create</button>
        </form>
      </div>
    )
  }
}

const mapStateToProps = (state, props) => {
  const categories = ['', 'Pizzeria', 'Mexican', 'Burger place']
  return {
    categories,
  }
}

export default withRouter(connect(mapStateToProps)(NewRestaurant));