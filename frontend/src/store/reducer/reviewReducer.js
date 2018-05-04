// import { GET_REVIEWS } from '../constants';


// const reviewsReducer = (state = [], action) => {
//     switch (action.type) {
//       case GET_REVIEWS:
//       const newState = action.payload.reviews.reduce((acc, review) => {
//         acc[review._id] = review;
//         return acc;
//       }, {});

//         return Object.assign({}, state, newState);
//     //   case TOGGLE_FOLLOW:
//         // const newUser = { ...state };
//     //     const toggleFollowId = action.payload.userId;
//     //     newUser.follows = newUser.follows.indexOf(toggleFollowId) > -1
//     //       ? newUser.follows.filter(followId => followId !== toggleFollowId)
//     //       : [...newUser.follows, toggleFollowId];
  
//     //     return newUser;
//     //   case REMOVE_CURRENT_USER:
//     //     return {};
//       default:
//         return state;
//     }
//   }