import { GET_DENUNCIA, DELETE_DENUNCIA, ADD_DENUNCIA } from "../actions/types";

const initialState = {
  denuncias: []
};

export default function(state = initialState, action) {
  switch (action.type) {
    case GET_DENUNCIA:
      return {
        ...state,
        denuncias: action.payload
      };
    case DELETE_DENUNCIA:
      return {
        ...state,
        denuncias: state.denuncias.filter(
          denuncias => denuncias.id !== action.payload
        )
      };
    case ADD_DENUNCIA:
      return {
        ...state,
        denuncias: [...state.denuncias, action.payload]
      };
    default:
      return state;
  }
}
