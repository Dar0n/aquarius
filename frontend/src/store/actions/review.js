import { SERVER_URL } from '../constants';
import { GET_REVIEWS } from '../constants';


const getReviews = (reviews) => ({
  type: GET_REVIEWS,
  payload: { reviews }
});



export const reviewAction = (state, props) => {
    return (dispatch, getState) => {
      const headers = new Headers({
        'content-type': 'application/json',
      })
      const config = {
        method: 'GET',
        headers: headers,
      }
      console.log("Before Fetch")
      fetch(SERVER_URL + 'reviews/restaurant/2/', config)
        .then(response => {
            console.log("response");
            console.log(response.json);
            return response.json();
        }).then(reviews =>{
          console.log('reviews')
          console.log(reviews)
        })
    }
  }