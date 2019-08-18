import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import {
  getDenunciasUsuario,
  deleteDenunciaUsuario
} from "../../actions/denunciasUsuario";

export class DenunciasUsuario extends Component {
  static propTypes = {
    denunciasUsuario: PropTypes.array.isRequired,
    getDenunciasUsuario: PropTypes.func.isRequired,
    deleteDenunciaUsuario: PropTypes.func.isRequired
  };

  componentDidMount() {
    this.props.getDenunciasUsuario();
  }

  render() {
    return (
      <Fragment>
        <h2>Lista de Denúncias do usuário</h2>
        <table className="table table-striped">
          <thead>
            <tr>
              <th>ID</th>
              <th>Latitude</th>
              <th>Longitude</th>
              <th>Denuncia</th>
              <th>criado em</th>
              <th />
            </tr>
          </thead>
          <tbody>
            {this.props.denunciasUsuario.map(denunciaUsuario => (
              <tr key={denunciaUsuario.id}>
                <td>{denunciaUsuario.id}</td>
                <td>{denunciaUsuario.latitude}</td>
                <td>{denunciaUsuario.longitude}</td>
                <td>{denunciaUsuario.denuncia}</td>
                <td>{denunciaUsuario.created_at}</td>
                <td>
                  <button
                    onClick={this.props.deleteDenunciaUsuario.bind(
                      this,
                      denunciaUsuario.id
                    )}
                    className="btn btn-danger btn-sm"
                  >
                    Delete
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </Fragment>
    );
  }
}

const mapStateToProps = state => ({
  denunciasUsuario: state.denunciasUsuario.denunciasUsuario
});

export default connect(
  mapStateToProps,
  { getDenunciasUsuario, deleteDenunciaUsuario }
)(DenunciasUsuario);
