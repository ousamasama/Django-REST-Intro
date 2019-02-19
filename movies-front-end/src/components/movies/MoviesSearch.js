import React, { Component } from 'react'

export default class MoviesSearch extends Component {
    state = {
        keyword: null
    }

    searchMovies = () => {
        this.props.search("movies", this.state.keyword)
    }

    setKeyword = (event) => {
        this.setState({keyword: event.target.value})
    }

    render() {
        return(
            // React Fragment shortcut
            <>
                <input type='text' onChange={this.setKeyword} placeholder="Search for Movies(Title)"/>
                <button onClick={this.searchMovies}>Search</button>
            </>
        )
    }
}