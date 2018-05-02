import { getTokens } from './getTokens';
import { SERVER_URL } from '../constants';

export const signupAction = (state, props) => {
  return (dispatch, getState) => {
    if(!state.email) {
      alert('You should fill the email field');
      return;
    }
    const body = {
      email: state.email,
    }
    const headers = new Headers({
      'content-type': 'application/json',
    })
    const config = {
      method: 'POST',
      body: JSON.stringify(body),
      headers: headers,
    }
    fetch(SERVER_URL + 'registration/', config)
      .then(response => {
        // console.log(response);
        if (response.status === 200) {
          props.history.push('/', {username: state.email});
        }
        else if (response.status === 400) {
          alert('Bad e-mail format or user with this email already exists.');
        }
        return response.json();
      })
  }
}

export const validationSubmitAction = (state, props, signUpState) => {
  return (dispatch, getState) => {
    if (!state.code || !state.password || !state.password_repeat || !state.first_name || !state.last_name) {
      alert('Not all fields filled');
    }
    else {
      const body = {
        code: state.code,
        password: state.password,
        password_repeat: state.password_repeat,
        first_name: state.first_name,
        last_name: state.last_name,
      }
      const headers = new Headers({
        'content-type': 'application/json',
      })
      const config = {
        method: 'POST',
        body: JSON.stringify(body),
        headers,
      }
      fetch('http://savchenko-ilya.propulsion-learn.ch/api/registration/validation/', config)
      .then(response => {
        // console.log(response);
        return response.json()
      })
      .then(data => {
        // console.log(data);
        const body = {
          username: signUpState.username,
          password: state.password,
        }
        getTokens(body, props, dispatch, getState);
      })
    }
  }
}