export const fetchFeed = content => dispatch => {
  const token = JSON.parse(localStorage.getItem("token"));
  const headers = new Headers({
    "content-type": "application/json"
  });
  const body = JSON.stringify(content);
  console.log("in the fetchFeed", body);
  const config = {
    headers: headers,
    body: body,
    method: "GET"
  };
  fetch("http://aquarius.propulsion-learn.ch/backend/api/restaurants", config)
    .then(res => res.json())
    .then(data => {
      dispatch(postFeed(data));
    });
};
