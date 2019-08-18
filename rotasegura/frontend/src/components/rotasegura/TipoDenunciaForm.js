import React, { Component } from "react";
import { connect } from "react-redux";
import { addTipoDenuncia } from "../../actions/tipoDenuncias";
import PropTypes from "prop-types";

export class TipoDenunciaForm extends Component {
  state = {
    descricao: ""
  };

  static propTypes = {
    addTipoDenuncia: PropTypes.func.isRequired
  };

  onChange = e => {
    this.setState({
      [e.target.name]: e.target.value
    });
  };

  onSubmit = e => {
    e.preventDefault();
    const { descricao } = this.state;
    const tipo_denuncia = { descricao };

    this.props.addTipoDenuncia(tipo_denuncia);

    this.setState({
      descricao: "",
      alreadyAdded: true
    });
  };

  render() {
    const { descricao } = this.state;
    return (
      <div className="container">
        <div className="card card-body mt-4 mb-4">
          <h2>Adicionar Tipo de Denuncia</h2>
          <form onSubmit={this.onSubmit}>
            <div className="form-group">
              <label>Descricao</label>
              <input
                className="form-control"
                type="text"
                name="descricao"
                onChange={this.onChange}
                value={descricao}
              />
            </div>
            <div className="form-group">
              <button type="submit" className="btn btn-primary">
                Submit
              </button>
            </div>
          </form>
        </div>
      </div>
    );
  }
}

export default connect(
  null,
  { addTipoDenuncia }
)(TipoDenunciaForm);
