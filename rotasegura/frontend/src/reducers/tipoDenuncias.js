import {
  GET_TIPO_DENUNCIA,
  DELETE_TIPO_DENUNCIA,
  ADD_TIPO_DENUNCIA
} from "../actions/types";

const initialState = {
  tipoDenuncias: []
};

export default function(state = initialState, action) {
  switch (action.type) {
    case GET_TIPO_DENUNCIA:
      return {
        ...state,
        tipoDenuncias: action.payload
      };
    case DELETE_TIPO_DENUNCIA:
      return {
        ...state,
        tipoDenuncias: state.tipoDenuncias.filter(
          tipoDenuncias => tipoDenuncias.id !== action.payload
        )
      };
    case ADD_TIPO_DENUNCIA:
      return {
        ...state,
        tipoDenuncias: [...state.tipoDenuncias, action.payload]
      };
    default:
      return state;
  }
}
