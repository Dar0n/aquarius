import { createStore, applyMiddleware, combineReducers } from 'redux';
import thunk from 'redux-thunk';

import { tokens } from './reducers/tokens';
import { loginStatus } from './reducers/loginStatus';
import { reviewsReducer } from './reducers/reviewsReducer';

const reducer = combineReducers({
  tokens,
  loginStatus,
  reviewsReducer,
})

const store = createStore(
  reducer,
  applyMiddleware(thunk),
);

export default store;