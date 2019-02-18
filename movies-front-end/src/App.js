import React, { Component } from 'react';
import './App.css';

class App extends Component {

  state = {
    movies: []
  }

  componentDidMount() {
    fetch('http://127.0.0.1:8000/movies')
    .then(stuff => stuff.json())
    .then(movies => {
      console.log(movies)
      // this.setState({movies: movies}) or
      this.setState({movies})
    })
  }

  render() {
    const movieNode = this.state.movies.map(movie => {
      return (<li key={movie.id}>{movie.title}</li>)
    })

    return (
      <div className="App">
        <h1>Daniel</h1>
        <ul>
          {/* when you pass array of elements it knows to create one of each */}
          {movieNode}
        </ul>
      </div>
    );
  }
}

export default App;
