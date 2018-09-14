const API_ADDRESS = 'http://127.0.0.1'

export function getLocations(name) {
  let data = $.ajax({
    url: API_ADDRESS + '/locations',
    data: { city: name },
    async: false,
    dataType: 'json'
  }).responseText;

  data = JSON.parse(data)
  return data.locations;
}

export function getSummary(startDate, endDate, locations) {
  console.log('STAR<+<END', startDate, endDate)
  let data = $.ajax({
    url: API_ADDRESS + '/summary',
    data: { startDate, endDate, locations: JSON.stringify(locations) },
    method: 'POST',
    async: false
  }).responseText;

  data = JSON.parse(data)
  return data.locations;
}

export function getPlaceDetails(name) {
  let data = $.ajax({
    url: API_ADDRESS + '/recommendation',
    data: { name },
    async: false
  }).responseText;

  data = JSON.parse(data)
  return data.locations[0];
}

export function getWiki(name) {

  let data = $.ajax({
    url: API_ADDRESS + '/getWiki',
    data: { name },
    async: false
  }).responseText;

  console.log('data', data)

  data = JSON.parse(data)
  console.log('data', data)
  return data;
}
