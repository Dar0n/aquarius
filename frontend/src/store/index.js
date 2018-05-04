import { createStore, applyMiddleware, combineReducers } from 'redux';
import thunk from 'redux-thunk';

import { tokens } from './reducers/tokens';
import { loginStatus } from './reducers/loginStatus';
import { localUser } from './reducers/localUser';

const reducer = combineReducers({
  tokens,
  loginStatus,
  localUser,
})

const store = createStore(
  reducer,
  applyMiddleware(thunk),
);

export default store;