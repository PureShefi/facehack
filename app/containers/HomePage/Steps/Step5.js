import React from 'react';
import TextField from 'material-ui/TextField';
import {Tabs, Tab} from 'material-ui/Tabs';
import {List, ListItem} from 'material-ui/List';
import Checkbox from 'material-ui/Checkbox';
import Dialog from 'material-ui/Dialog';
import FlatButton from 'material-ui/FlatButton';
import RaisedButton from 'material-ui/RaisedButton';

import { getSummary, getWiki } from './StepsAjaxCalls.js'

const plan = [{ weather: { lowestTemp: '20', heighestTemp: '40', description: 'very sunny' }, places: ['ny', 'ca'] },
              { weather: { lowestTemp: '20', heighestTemp: '40', description: 'cloudy' }, places: ['Times Square, Manhattan, NY, USA','M&M\'S World, Broadway, Manhattan, New York, NY, USA', 'Apple Fifth Avenue, 5th Avenue, New York, NY, USA'] },
            { weather: { lowestTemp: '20', heighestTemp: '40', description: '' }, places: ['ChIJp-0cdPBYwokRRNGjt9080k8', 'ChIJp-0cdPBYwokRRNGjt9080k8'] },
          { weather: { lowestTemp: '20', heighestTemp: '40', description: 'lots of rain' }, places: [''] },
        { weather: { lowestTemp: '20', heighestTemp: '40', description: 'very sunny' }, places: [''] },]

export default class Step5 extends React.PureComponent {
  /**
   * when initial state username is not null, submit the form to load repos
   */

  constructor(props) {
   super(props);

   this.state = {
     plan: getSummary(this.props.formvalue.minDate, this.props.formvalue.maxDate, this.props.formvalue.popularPlaces.concat(this.props.formvalue.customPlaces)),
     value: -1,
     open: false,
     dialogName: ''
   }

   this.initMap = this.initMap.bind(this);
   this.initMaps = this.initMaps.bind(this);
   this.handleChange = this.handleChange.bind(this);
   this.getAllLocations = this.getAllLocations.bind(this);
  }

  getAllLocations() {
    let locations = [];

    this.state.plan.map((value) => {
      value.locations.map((location) => {
        locations.push(location)
      })
    });

    return locations;
  }

  initMaps() {
    this.initMap("map", this.getAllLocations().map((value) => { return value.geometry.location; }))
    this.state.plan.map((value, index) => {
      this.initMap("map" + index.toString(), value.locations.map((value) => { return value.geometry.location; }))
    })
  }

  initMap(id, route) {
    var directionsService = new google.maps.DirectionsService;
    var directionsDisplay = new google.maps.DirectionsRenderer;
    var map = new google.maps.Map(document.getElementById(id), {
      zoom: 13,
      center: route[0]
    });
    directionsDisplay.setMap(map);

    if (id === 'map') {
      route.map((value) => {
        console.log(value)
        let marker = new google.maps.Marker({
          map: map,
          draggable: true,
          animation: google.maps.Animation.DROP,
          position: value
        });
      })
      return;
    }

    this.calculateAndDisplayRoute(directionsService, directionsDisplay, route);
  }

  calculateAndDisplayRoute(directionsService, directionsDisplay, route) {
    let origin = route[0]
    let dest = route[route.length - 1]
    let onTheWay = []
    let current = route.slice(1, route.length - 1)
    current.map((value) => {
      onTheWay.push({ location: value, stopover: true })
    })
    directionsService.route({
      origin: origin,
      destination: dest,
      travelMode: 'DRIVING',
      waypoints: onTheWay
    }, function(response, status) {
      if (status === 'OK') {
        directionsDisplay.setDirections(response);
      } else {
        window.alert('Directions request failed due to ' + status);
      }
    });
  }

  componentDidMount() {
    this.initMaps();
  }

  handleChange = (value) => {
    this.setState({
      value: value,
    });
  }

  handleOpen = () => {
    this.setState({open: true});
  };

  handleClose = () => {
    this.setState({open: false});
  };

 mapStyle = { height: '400px', width: '800px' }
 detailsStyle = { height: '400px', width: '263px', overflow: 'hidden', overflowY: 'auto', float: 'left' }

  render() {

    const actions = [
      <FlatButton
        label="Close"
        primary={true}
        onClick={this.handleClose}
      />,
    ];

    const Locations = ({locations}) => {
      return(
        <List>
          {locations.map((place, index) => {
            return <ListItem
            primaryText={place.name}
            leftIcon={<div style={{ width: '42px' }}>
              <img style={{ height: '30px', float: 'left' }} src={require('../../../images/wikipedia.png')} onClick={() => this.setState({ open: true, dialogName: place.name })} />
              </div>}
            />
          })}
        </List>
      )
    }


    return (
      <div>
        <Dialog
          title={"Wikipedia For" + this.state.dialogName}
          actions={actions}
          contentStyle={{ maxWidth: 'none', width: '90%', maxHeight: 'none', height: '1200px' }}
          open={this.state.open}
        >
          {this.state.open && <iframe src={getWiki(this.state.dialogName).url} style={{ width: '90%', height: '1500px', overflowY: 'auto'}}/>}


        </Dialog>
        <Tabs
          value={this.state.value}
          onChange={this.handleChange}
        >
        <Tab label={"Overall Plan"} value={-1}>
          <div>
            <div style={this.detailsStyle}>
              <Locations locations={this.getAllLocations()} />
            </div>
            <div id={"map"} style={this.mapStyle} ></div>
          </div>
        </Tab>
        {this.state.plan.map((plan, index) => {
          return <Tab label={"Day " + (index+1).toString()} value={index}>
            <div>
              <div style={this.detailsStyle}>
                <Weather weather={plan.weather} />
                <Locations locations={plan.locations} />
              </div>
              <div id={"map" + index.toString()} style={this.mapStyle} ></div>
            </div>
          </Tab>
        })}
        </Tabs>
      </div>
    );
  }
}

const getWeatherPic = (description) => {
  let data = description.toLowerCase();
  if (data.includes('shower') || data.includes('rain')) return <img style={{ height: '100px'}} src={require('../../../images/rain.png')} />
  if (data.includes('sun') || data.includes('hot')) return <img style={{ height: '100px'}} src={require('../../../images/sun.png')} />
  if (data.includes('cloud')) return <img style={{ height: '100px'}} src={require('../../../images/cloudy.png')} />
  return <div />
}

const Weather = ({weather}) => {
  return(
    <div style={{ textAlign: 'center' }}>
      <div >
        {getWeatherPic(weather.text)}
      </div>
      {weather.date}
      <br />
      {weather.text}
      <br />
      Lowest Temp: {weather.low}
      <br />
      Heighest Temp: {weather.high}
    </div>
  )
}
