import { SERVER_URL } from '../constants';
import { validateTokens } from './validateTokens';

export const fetchUserInfo = (props) => {
  return (dispatch, getState) => {
    console.log(getState());
    const headers = ({
      Authorization: `Bearer ${getState().tokens.access}`,
    });
    const config = {
      method: 'GET',
      headers,
    }
    const state = getState();
    validateTokens(state, dispatch, props)
    .then(response => fetch(SERVER_URL + 'me/', config))
    .then(response => {
      console.log(response);
      return response.json();
    })
    .then(data => {
      console.log(data);
    })
  }
}