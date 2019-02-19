import React, { Component } from 'react';

export default class MoviesForm extends Component {
    state = {
        title: '',
        year: ''
    }

    handleFieldChange = (event) => {
        const stateToChange = {}
        stateToChange[event.target.id] = event.target.value
        this.setState(stateToChange)
    }

    clearForm(){
        document.getElementById("title").value = "";
        document.getElementById("year").value = "";
    }

    submitAndClear(){
        this.props.create("movies", this.state);
        this.clearForm();
    }

    render() {
        return(
            <>
                <h3>Add a new movie to the collection!</h3>
                <input 
                    type='text'
                    id='title'
                    placeholder='movie title'
                    onChange={this.handleFieldChange}
                />
                <input 
                    type='text'
                    id='year'
                    placeholder='movie year released'
                    onChange={this.handleFieldChange}
                />
                <button onClick={() => this.submitAndClear()}>
                    Submit New Movie
                </button>
            </>
        )
    }
}