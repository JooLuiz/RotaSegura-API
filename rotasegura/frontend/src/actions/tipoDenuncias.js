import axios from "axios";
import { createMessage, returnErrors } from "./messages";
import {
  GET_TIPO_DENUNCIA,
  DELETE_TIPO_DENUNCIA,
  ADD_TIPO_DENUNCIA
} from "./types";
import { tokenConfig } from "./auth";

//GET Tipo de Denuncia
export const getTipoDenuncias = () => (dispatch, getState) => {
  axios
    .get("/api/tipodenuncia/", tokenConfig(getState))
    .then(res => {
      dispatch({
        type: GET_TIPO_DENUNCIA,
        payload: res.data
      });
    })
    .catch(err =>
      dispatch(returnErrors(err.response.data, err.response.status))
    );
};

//DELETE Tipo de denuncia

export const deleteTipoDenuncia = id => (dispatch, getState) => {
  axios
    .delete(`/api/tipodenuncia/${id}/`, tokenConfig(getState))
    .then(res => {
      dispatch(
        createMessage({ deleteTipoDenuncia: "Tipo de Denúncia Deletada!" })
      );
      dispatch({
        type: DELETE_TIPO_DENUNCIA,
        payload: id
      });
    })
    .catch(err =>
      dispatch(returnErrors(err.response.data, err.response.status))
    );
};

//ADD Tipo de denuncia
export const addTipoDenuncia = TipoDenuncia => (dispatch, getState) => {
  axios
    .post("/api/tipodenuncia/", TipoDenuncia, tokenConfig(getState))
    .then(res => {
      dispatch(
        createMessage({ addTipoDenuncia: "Tipo de Denúncia Registrada" })
      );
      dispatch({
        type: ADD_TIPO_DENUNCIA,
        payload: res.data
      });
    })
    .catch(err =>
      dispatch(returnErrors(err.response.data, err.response.status))
    );
};
