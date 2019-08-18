import { combineReducers } from "redux";
import errors from "./errors";
import messages from "./messages";
import auth from "./auth";
import denunciasUsuario from "./denunciasUsuario";
import tipoDenuncias from "./tipoDenuncias";
import denuncias from "./denuncias";

export default combineReducers({
  errors,
  messages,
  auth,
  denunciasUsuario,
  tipoDenuncias,
  denuncias
});
