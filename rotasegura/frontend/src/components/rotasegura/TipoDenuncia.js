import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import {
  getTipoDenuncias,
  deleteTipoDenuncia,
  addTipoDenuncia
} from "../../actions/tipoDenuncias";
import { TipoDenunciaForm } from "./TipoDenunciaForm";

export class TipoDenuncia extends Component {
  static propTypes = {
    tipoDenuncias: PropTypes.array.isRequired,
    getTipoDenuncias: PropTypes.func.isRequired,
    deleteTipoDenuncia: PropTypes.func.isRequired,
    addTipoDenuncia: PropTypes.func.isRequired
  };

  componentDidMount() {
    this.props.getTipoDenuncias();
  }

  render() {
    return (
      <Fragment>
        <TipoDenunciaForm addTipoDenuncia={this.props.addTipoDenuncia} />
        <br />
        <h2>Lista de Tipos de Denúncias</h2>
        <table className="table table-striped">
          <thead>
            <tr>
              <th>ID</th>
              <th>Descricao</th>
              <th>Criado em</th>
              <th />
            </tr>
          </thead>
          <tbody>
            {this.props.tipoDenuncias.map(tipoDenuncia => (
              <tr key={tipoDenuncia.id}>
                <td>{tipoDenuncia.id}</td>
                <td>{tipoDenuncia.descricao}</td>
                <td>{tipoDenuncia.created_at}</td>
                <td>
                  <button
                    onClick={this.props.deleteTipoDenuncia.bind(
                      this,
                      tipoDenuncia.id
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
  tipoDenuncias: state.tipoDenuncias.tipoDenuncias
});

export default connect(
  mapStateToProps,
  { getTipoDenuncias, deleteTipoDenuncia, addTipoDenuncia }
)(TipoDenuncia);
