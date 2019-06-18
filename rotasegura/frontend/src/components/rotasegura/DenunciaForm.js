import React, { Component } from "react";
import { connect } from "react-redux";
import { addDenuncia } from "../../actions/denuncias";
import PropTypes from "prop-types";

export class DenunciaForm extends Component {
  state = {
    descricao: "",
    tipo_denuncia: ""
  };

  static propTypes = {
    addDenuncia: PropTypes.func.isRequired
  };

  onChange = e => {
    this.setState({
      [e.target.name]: e.target.value
    });
  };

  onSubmit = e => {
    e.preventDefault();
    const { descricao, tipo_denuncia } = this.state;
    const denuncia = { descricao, tipo_denuncia };

    this.props.addDenuncia(denuncia);

    this.setState({
      descricao: "",
      tipo_denuncia: ""
    });
  };

  render() {
    const { descricao, tipo_denuncia } = this.state;
    return (
      <div className="container">
        <div className="card card-body mt-4 mb-4">
          <h2>Adicionar Categoria de Denuncia</h2>
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
              <label>Tipo Denúncia</label>
              <input
                className="form-control"
                type="number"
                min="1"
                name="tipo_denuncia"
                onChange={this.onChange}
                value={tipo_denuncia}
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
  { addDenuncia }
)(DenunciaForm);
