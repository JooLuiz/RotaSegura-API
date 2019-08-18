import axios from "axios";
import { createMessage, returnErrors } from "./messages";
import { GET_DENUNCIA, DELETE_DENUNCIA, ADD_DENUNCIA } from "./types";
import { tokenConfig } from "./auth";

//GET  de Denuncia
export const getDenuncias = () => (dispatch, getState) => {
  axios
    .get("/api/denuncias/", tokenConfig(getState))
    .then(res => {
      dispatch({
        type: GET_DENUNCIA,
        payload: res.data
      });
    })
    .catch(err =>
      dispatch(returnErrors(err.response.data, err.response.status))
    );
};

//DELETE de denuncia

export const deleteDenuncia = id => (dispatch, getState) => {
  axios
    .delete(`/api/denuncias/${id}/`, tokenConfig(getState))
    .then(res => {
      dispatch(
        createMessage({ deleteDenuncia: "Categoria da Denúncia Deletada!" })
      );
      dispatch({
        type: DELETE_DENUNCIA,
        payload: id
      });
    })
    .catch(err =>
      dispatch(returnErrors(err.response.data, err.response.status))
    );
};

//ADD de denuncia
export const addDenuncia = Denuncia => (dispatch, getState) => {
  axios
    .post("/api/denuncias/", Denuncia, tokenConfig(getState))
    .then(res => {
      dispatch(
        createMessage({ addDenuncia: "Categoria da Denúncia Registrada" })
      );
      dispatch({
        type: ADD_DENUNCIA,
        payload: res.data
      });
    })
    .catch(err =>
      dispatch(returnErrors(err.response.data, err.response.status))
    );
};
