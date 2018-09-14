import React from 'react';
import TextField from 'material-ui/TextField';
import DatePicker from 'material-ui/DatePicker';

const optionsStyle = {
  maxWidth: 255,
  marginRight: 'auto',
};

/**
 * This example allows you to set a date range, and to toggle `autoOk`, and `disableYearSelection`.
 */
export default class Step1 extends React.Component {
  constructor(props) {
    super(props);

    const minDate = Date.now();
    const maxDate = Date.now();

    this.props.actions({
      minDate: minDate,
      maxDate: maxDate,
      city: ''
    });
  }

  handleChangeMinDate = (event, date) => {
    this.props.actions({
      minDate: date.getMilliseconds(),
    });
  };

  handleChangeMaxDate = (event, date) => {
    this.props.actions({
      maxDate: date.getMilliseconds(),
    });
  };

  componentDidMount() {
    // var defaultBounds = new google.maps.LatLngBounds(
    // new google.maps.LatLng(-33.8902, 151.1759),
    // new google.maps.LatLng(-33.8474, 151.2631));

    var input = document.getElementById('citySearcher');

    var searchBox = new google.maps.places.SearchBox(input, {
      types: ['(cities)']
    });
  }

  render() {
    console.log('this.props', this.props.formvalue.city)

    return (
      <div>

        <TextField
          floatingLabelText="Enter City"
          id='citySearcher'
          value={this.props.formvalue.city}
          placeHolder=''
          onChange={(event, newValue) => this.props.actions({ city: newValue })}
        />
        <div style={optionsStyle}>
          <DatePicker
            onChange={this.handleChangeMinDate}
            autoOk
            floatingLabelText="Arrival Date"
            local='en-GB'
            value={new Date(this.props.formvalue.minDate)}
            onChange={(event, newValue) => this.props.actions({ minDate: newValue.getTime() })}
          />
          <DatePicker
            onChange={this.handleChangeMaxDate}
            autoOk
            floatingLabelText="Departure Date"
            value={new Date(this.props.formvalue.maxDate)}
            onChange={(event, newValue) => this.props.actions({ maxDate: newValue.getTime() })}
          />
        </div>
      </div>
    );
  }
}
