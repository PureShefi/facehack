import React from 'react';
import Flippy, { FrontSide, BackSide } from 'react-flippy';

import { getLocations } from './StepsAjaxCalls.js'

const places = [{ name: 'Statue of Liberty', data: 'some Shit', imageUrl: "https://lh5.googleusercontent.com/proxy/AOkBLny9SJ-4jnhFyhZV_MZfA-xpqBht7hU37jrYFjm6bnFeGUP_DeFQ_MdAd-B5r8MgIg1bwWbXFsEOETQdq9vFU1fjqbR9sD1rTO3NhDBZC8WAHzuIW295Dd6xTiensrWnE3ySc2Xey0dvtp3KVA_Ktvs=w100-h134-n-k-no" },
           { name: 'Statue of Liberty', data: 'some Shit', imageUrl: "https://lh5.googleusercontent.com/proxy/AOkBLny9SJ-4jnhFyhZV_MZfA-xpqBht7hU37jrYFjm6bnFeGUP_DeFQ_MdAd-B5r8MgIg1bwWbXFsEOETQdq9vFU1fjqbR9sD1rTO3NhDBZC8WAHzuIW295Dd6xTiensrWnE3ySc2Xey0dvtp3KVA_Ktvs=w100-h134-n-k-no" },
           { name: 'Statue of Liberty', data: 'some Shit', imageUrl: "https://lh5.googleusercontent.com/proxy/AOkBLny9SJ-4jnhFyhZV_MZfA-xpqBht7hU37jrYFjm6bnFeGUP_DeFQ_MdAd-B5r8MgIg1bwWbXFsEOETQdq9vFU1fjqbR9sD1rTO3NhDBZC8WAHzuIW295Dd6xTiensrWnE3ySc2Xey0dvtp3KVA_Ktvs=w100-h134-n-k-no" }
]


const unselectedLocationStyle = {}
const selectedLocationStyle = { opacity: '0.4' }

/* eslint-disable react/prefer-stateless-function */
export default class Step2 extends React.PureComponent {
/**
* when initial state username is not null, submit the form to load repos
*/

  constructor(props) {
    super(props);

    let clickedArray = new Array(places.length);
    clickedArray.fill(false);
    this.state = {
      isClicked: clickedArray,
      places: getLocations(this.props.formvalue.city),
    }

    this.onFlipClick = this.onFlipClick.bind(this);
  }

  onFlipClick (index) {
    this.state.isClicked[index] = !this.state.isClicked[index]
    console.log('isClicked', this.state.isClicked)

    let currentPlaces = []
    this.state.isClicked.map((value,index) => {
      if (value) currentPlaces.push(this.state.places[index])
    })

    this.props.actions({ popularPlaces: currentPlaces })

    this.forceUpdate();
  }

  render() {

  let style = unselectedLocationStyle;
  if (this.state.isClicked) style = selectedLocationStyle

  return (
    <div style={{ display: 'flex', flex: '1 0 200px', justifyContent: 'space-around', 'flex-wrap': 'wrap', width: '1067px', height: '450px', overflow: 'hidden', overflowY: 'auto', padding: '10px 0 10px 0' }}>

      {this.state.places.map((location, index) => {
        let currentStyle = unselectedLocationStyle;
        if (this.state.isClicked[index]) currentStyle = selectedLocationStyle;
        return (
          <div id='sfas' onClick={() => this.onFlipClick(index)} style={Object.assign({ height: '200px', width: '200px', maxWidth: '200px' }, currentStyle)}>
          <FlipCard
            name={location.name}
            imageUrl={location.photos[0].photo_reference}
            data={location.rating}
            style={style}
          />
        </div>
    )
      })}

    </div>
    );
  }
}


const FlipCard = ({name, imageUrl, data, style}) => {
  return(
    <Flippy
      flipOnHover
      flipDirection="horizontal" // horizontal or vertical
      // ref={(r) => this.flippy = r} // to use toggle method like this.flippy.toggle()
      // if you pass isFlipped prop component will be controlled component.
      // and other props, which will go to div
      style={{ width: '200px', height: '200px' }} /// these are optional style, it is not necessary
    >
      <FrontSide
        style={{
          backgroundImage: 'url(' + 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference=' + {imageUrl} + '&key=AIzaSyAtVGYjp7gGHRu0YcoRAxyB_IruztcMx1s' + ')',
          backgroundSize: 'cover'
        }}
      >
      <div style={{ overflow: 'hidden', height: '140px' }}>
        <iframe style={{ position: 'relative', left: '-100px', top: '-65px', height: '300px' }} src={'https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference=' + imageUrl + '&key=AIzaSyAtVGYjp7gGHRu0YcoRAxyB_IruztcMx1s'} />
      </div>
        {name}
      </FrontSide>
      <BackSide
        style={{ backgroundColor: '#41addd' }}>
        <p style={{ maxHeight: '150px', overflow: 'hidden', overflowY: 'auto' }}>
          Rating: {data}
        </p>
      </BackSide>
    </Flippy>)
}
