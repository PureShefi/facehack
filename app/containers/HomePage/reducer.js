import { fromJS } from 'immutable';

import { CHANGE_USERNAME } from './constants';

// The initial state of the App
export const initialState = fromJS({
  username: {
    name: '',
    minDate: {},
    maxDate: {},
    selectedLocations: []
  },
});

function homeReducer(state = initialState, action) {
  switch (action.type) {
    case CHANGE_USERNAME:
      // Delete prefixed '@' from the github username
      return state.set('username', Object.assign({}, state.username, action.name));
    default:
      return state;
  }
}

export default homeReducer;
