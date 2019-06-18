import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import {
  getDenuncias,
  deleteDenuncia,
  addDenuncia
} from "../../actions/denuncias";
import { DenunciaForm } from "./DenunciaForm";

export class Denuncia extends Component {
  static propTypes = {
    denuncias: PropTypes.array.isRequired,
    getDenuncias: PropTypes.func.isRequired,
    deleteDenuncia: PropTypes.func.isRequired,
    addDenuncia: PropTypes.func.isRequired
  };

  componentDidMount() {
    this.props.getDenuncias();
  }

  render() {
    return (
      <Fragment>
        <DenunciaForm addDenuncia={this.props.addDenuncia} />
        <br />
        <h2>Lista de Categorias de Denúncias</h2>
        <table className="table table-striped">
          <thead>
            <tr>
              <th>ID</th>
              <th>Descricao</th>
              <th>Tipo da Denúncia</th>
              <th>Criado em</th>
              <th />
            </tr>
          </thead>
          <tbody>
            {this.props.denuncias.map(denuncia => (
              <tr key={denuncia.id}>
                <td>{denuncia.id}</td>
                <td>{denuncia.descricao}</td>
                <td>{denuncia.tipo_denuncia}</td>
                <td>{denuncia.created_at}</td>
                <td>
                  <button
                    onClick={this.props.deleteDenuncia.bind(this, denuncia.id)}
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
  denuncias: state.denuncias.denuncias
});

export default connect(
  mapStateToProps,
  { getDenuncias, deleteDenuncia, addDenuncia }
)(Denuncia);
