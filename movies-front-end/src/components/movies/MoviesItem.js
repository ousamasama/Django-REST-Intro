import React, {Component} from "react"

export default class MoviesItem extends Component {
    render() {
        return(<li>{this.props.movie.title}
        <button onClick={() => this.props.delete(this.props.movie.id)}>Delete</button>
        </li>)
    }
}