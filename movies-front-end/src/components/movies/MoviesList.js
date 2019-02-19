import React, { Component } from 'react';
import MoviesItem from "./MoviesItem"

export default class MoviesList extends Component {
    componentDidMount() {
        this.props.getAll("movies")
    }

    render() {
        const movieNode = this.props.movies.map((movie) => {
            return (<MoviesItem movie={movie} key={movie.id} delete={this.props.delete} />)
        })

        return (
            <div className="movie-container">
                <h2>A list of movies</h2>
                <ul>{movieNode}</ul>
            </div>
        )
    }
}