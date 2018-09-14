import React from 'react';
import TextField from 'material-ui/TextField';
import {List, ListItem} from 'material-ui/List';
import Checkbox from 'material-ui/Checkbox';

import { getPlaceDetails } from './StepsAjaxCalls.js'

const width = '500px';

export default class Step3 extends React.PureComponent {
  /**
   * when initial state username is not null, submit the form to load repos
   */

  constructor(props) {
   super(props);
   this.state = {
     currentValue: '',
     places: [],
     checkedPlaces: []
   }

   this.addPlace = this.addPlace.bind(this);
   this.submit = this.submit.bind(this);
   this.onCheck = this.onCheck.bind(this);
   this.updateForm = this.updateForm.bind(this);
  }

  componentDidMount() {
    var input = document.getElementById('placeSearcher');

    var searchBox = new google.maps.places.SearchBox(input, {
      types: ['(cities)']
    });
  }

  addPlace() {
    let element = document.getElementById('placeSearcher');
    let value = getPlaceDetails(element.value);
    console.log('Value', value)
    if (0 === this.state.places.filter((a) => { if (a.name === value.name) return true }).length){
      this.state.places.push(value);
      this.state.checkedPlaces.push(true)
    }
    this.forceUpdate();
    this.updateForm();
  }

  submit(e) {
    e.preventDefault();
    this.addPlace();
  }

  onCheck (isInputChecked, index) {
    this.state.checkedPlaces[index] = isInputChecked;
    this.forceUpdate();
    this.updateForm();
  }

  updateForm() {
    let currentPlaces = []
    this.state.checkedPlaces.map((value,index) => {
      if (value) currentPlaces.push(this.state.places[index])
    })

    this.props.actions({ customPlaces: currentPlaces })
  }

  render() {
    return (
      <div>
        <form onSubmit={this.submit} >
          <TextField
            floatingLabelText="Enter Location"
            id='placeSearcher'
            placeHolder=''
            style={{ width }}
          />
        </form>
        <div style={{ width, height: '200px', overflow: 'hidden', overflowY: 'auto' }}>
        <List>
          {this.state.places.map((place, index) => {
            return <ListItem
            primaryText={place.name}
            style={{ width }}
            leftCheckbox={<Checkbox checked={this.state.checkedPlaces[index]} onCheck={(event, isInputChecked) => this.onCheck(isInputChecked, index)} />}
            />
          })}
        </List>
        </div>
      </div>
    );
  }
}
