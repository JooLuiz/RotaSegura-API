import axios from "axios";
import { createMessage, returnErrors } from "./messages";
import {
  GET_DENUNCIAS_USUARIO,
  DELETE_DENUNCIA_USUARIO,
  ADD_DENUNCIA_USUARIO
} from "./types";
import { tokenConfig } from "./auth";

//GET Denuncia Usuario
export const getDenunciasUsuario = () => (dispatch, getState) => {
  axios
    .get("/api/usuario_denuncia/", tokenConfig(getState))
    .then(res => {
      dispatch({
        type: GET_DENUNCIAS_USUARIO,
        payload: res.data
      });
    })
    .catch(err =>
      dispatch(returnErrors(err.response.data, err.response.status))
    );
};

//DELETE Denuncia Usuário

export const deleteDenunciaUsuario = id => (dispatch, getState) => {
  axios
    .delete(`/api/usuario_denuncia/${id}/`, tokenConfig(getState))
    .then(res => {
      dispatch(createMessage({ deleteDenunciaUsuario: "Denúncia Deletada!" }));
      dispatch({
        type: DELETE_DENUNCIA_USUARIO,
        payload: id
      });
    })
    .catch(err =>
      dispatch(returnErrors(err.response.data, err.response.status))
    );
};

//ADD Denuncia Usuario

export const addDenunciaUsuario = DenunciaUsuario => (dispatch, getState) => {
  axios
    .post("/api/usuario_denuncia/", DenunciaUsuario, tokenConfig(getState))
    .then(res => {
      dispatch(createMessage({ addDenunciaUsuario: "Denúncia Registrada" }));
      dispatch({
        type: ADD_DENUNCIA_USUARIO,
        payload: res.data
      });
    })
    .catch(err =>
      dispatch(returnErrors(err.response.data, err.response.status))
    );
};
