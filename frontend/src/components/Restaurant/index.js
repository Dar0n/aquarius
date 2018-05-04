// import React, { Component } from 'react';
// import { connect } from 'react-redux';
// import { withRouter }  from 'react-router-dom';
//
// import './index.css';
//
//
// class RestaurantCard extends Component {
//
//   navigate = (e) => {
//
//   }
//
//   render() {
//     console.log('In da card!');
//     return (
//       <div className='RestaurantCard-main-container'>
//
//         <div className='RestaurantCard-list-container'>
//           <img className='RestaurantCard-img-top' src={props.restaurant.review} alt="restaurant-review" />
//           <div className='RestaurantCard-card-container'>
//             <h4 className='RestaurantCard-title'>{props.restaurant.name}</h4>
//             <h6 className='RestaurantCard-address'>{props.restaurant.address}</h6>
//             <p className='RestaurantCard-description'>{props.restaurant.content}</div>
//           </div>
//
//           <div className='RestaurantCard-footer'>
//             <div className='RestaurantCard-clearfix'>
//               <div className=''>
//                 <StarRating rating={props.restaurant.rating} />
//               </div>
//               <div className='RestaurantCard-rating'>{props.restaurant.rating}</div>
//             </div>
//
//           </div>
//         </div>
//
//
//         <div className='RestaurantCard-restaurant-container'>
//         </div>
//         <div className='Card-container'>
//         </div>
//
//       </div>
//     );
//   }
// }
//
// const mapStateToProps = (state, props) => {
//   return {
//
//   }
// }
//
// export default withRouter(connect(mapStateToProps)(RestaurantCard));