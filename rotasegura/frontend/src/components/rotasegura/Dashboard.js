import React, { Fragment } from "react";
import { Link } from "react-router-dom";
import DenunciasUsuario from "./DenunciasUsuario";

export default function Dashboard() {
  return (
    <Fragment>
      <Link to="/usuario_denuncia/new" className="btn btn-default">
        Realizar Denúncia
      </Link>
      <br />
      <DenunciasUsuario />
    </Fragment>
  );
}
