import {
  GET_DENUNCIAS_USUARIO,
  DELETE_DENUNCIA_USUARIO,
  ADD_DENUNCIA_USUARIO
} from "../actions/types";

const initialState = {
  denunciasUsuario: []
};

export default function(state = initialState, action) {
  switch (action.type) {
    case GET_DENUNCIAS_USUARIO:
      return {
        ...state,
        denunciasUsuario: action.payload
      };
    case DELETE_DENUNCIA_USUARIO:
      return {
        ...state,
        denunciasUsuario: state.denunciasUsuario.filter(
          denunciaUsuario => denunciaUsuario.id !== action.payload
        )
      };
    case ADD_DENUNCIA_USUARIO:
      return {
        ...state,
        denunciasUsuario: [...state.denunciasUsuario, action.payload]
      };
    default:
      return state;
  }
}
