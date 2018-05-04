import React, { Component } from 'react';
import { connect } from 'react-redux';
import { withRouter, Link }  from 'react-router-dom';
import {reviewAction} from '../../store/actions/review'

class Review extends Component{
    constructor(props){
        super(props)
        this.state = {
            content: "",
        }
    }
    render(){
        console.log(this.props, "handleFetchReviews")
        // this.props.reviewAction(this.state, this.props)
        return(
            <div className='Review-container'>
            <form className='Review-container-form' >
                    
                    <input 
                        type='text' 
                        placeholder='Review'
                    />
                    <button onClick={ this.handleFetchReviews }>Fetch Review</button>
                    </form>
            </div>
        )
    }
    handleFetchReviews = (e) =>{
        e.preventDefault();
        // console.log(this.props, "handleFetchReviews");
        this.props.dispatch(reviewAction(this.state, this.props));
        
    }

}


const mapStateToProps = (state, props) => {
    return {}
  }
  
export default withRouter(connect(mapStateToProps)(Review));