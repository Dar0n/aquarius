import { createStore, applyMiddleware, combineReducers } from "redux";
import thunk from "redux-thunk";
import { tokens } from './reducers/tokens';
import { loginStatus } from './reducers/loginStatus';
import { localUser } from './reducers/localUser';
import { restaurantReducer } from "./reducers/restaurantReducer";

const reducer = combineReducers({
  tokens,
  loginStatus,
  localUser,
  restaurantReducer,
});

const store = createStore(reducer, applyMiddleware(thunk));

export default store;
