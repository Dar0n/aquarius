import { createStore, applyMiddleware, combineReducers } from 'redux';
import thunk from 'redux-thunk';

import {tokens} from './tokens';

const reducer = combineReducers({
  tokens,
  
})

const store = createStore(
  reducer,
  applyMiddleware(thunk),
);

export default store;