import React, { Component } from 'react';
import MoviesList from "./components/movies/MoviesList"
import MoviesSearch from "./components/movies/MoviesSearch"
import MoviesForm from "./components/movies/MoviesForm"
import './App.css';

class App extends Component {

  state = {
    movies: [],
    apiURL: 'http://127.0.0.1:8000/api/v1'
  }

  // componentDidMount() {
  //   fetch('http://127.0.0.1:8000/movies')
  //   .then(stuff => stuff.json())
  //   .then(movies => {
  //     console.log(movies)
  //     // this.setState({movies: movies}) or
  //     this.setState({movies})
  //   })
  // }

  // TODO: Put API logic in a manager
  getAll = (resource, keyword = null) => {
    let url = `${this.state.apiURL}/${resource}/`
    // if only single statement you dont need curly
    if (keyword)
      url += keyword

    fetch(url)
      .then(response => response.json())
      .then(data => {
        console.log("movies list", data)
        this.setState({ [resource]: data })
      })
      .catch(err => console.log("Error", err))
  }

  search = (resource, keyword) => {
    let query = `?search=${keyword}`
    console.log("keyword", keyword)
    this.getAll(resource, query)
  }

  setMovieState = (movies) => this.setState({ movies })

  create = (resource, newObj) => {
    let formData = new FormData()
    for (let key in newObj) {
      formData.append(key, newObj[key])
    }

    fetch(`${this.state.apiURL}/${resource}/`, {
      method: 'POST',
      body: formData
    })
      .then(newData => newData.json())
      .then(newData => {
        console.log("added?", newData)
        this.getAll(resource)
      })
  }

  delete = (resource, id) => {
    return fetch(`${this.state.apiURL}/${resource}/${id}/`, {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify
    })
      .then(() => this.getAll(resource)
      )
  };

  render() {
    // const movieNode = this.state.movies.map(movie => {
    //   return (<li key={movie.id}>{movie.title}</li>)
    // })
    return (
      <div className="App">
        <h1>Daniel</h1>
        <MoviesSearch search={this.search} />
        <MoviesList movies={this.state.movies} setMovieState={this.setMovieState} delete={this.delete} getAll={this.getAll} />
        <MoviesForm create={this.create} />
      </div>
    );
  }
}

export default App;
