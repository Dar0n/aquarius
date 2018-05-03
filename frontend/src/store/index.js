import { createStore, applyMiddleware, combineReducers } from 'redux';
import thunk from 'redux-thunk';

import { tokens } from './reducers/tokens';
import { loginStatus } from './reducers/loginStatus';

const reducer = combineReducers({
  tokens,
  loginStatus,
})

const store = createStore(
  reducer,
  applyMiddleware(thunk),
);

export default store;