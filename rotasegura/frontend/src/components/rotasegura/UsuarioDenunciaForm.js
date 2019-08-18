import React, { Component } from "react";
import { connect } from "react-redux";
import { Link, Redirect } from "react-router-dom";
import PropTypes from "prop-types";
import { addDenunciaUsuario } from "../../actions/denunciasUsuario";

export class UsuarioDenunciaForm extends Component {
  state = {
    latitude: "",
    longitude: "",
    denuncia: "",
    alreadyAdded: false
  };

  static propTypes = {
    addDenunciaUsuario: PropTypes.func.isRequired
  };

  onChange = e => {
    this.setState({
      [e.target.name]: e.target.value
    });
  };

  onSubmit = e => {
    e.preventDefault();
    const { latitude, longitude, denuncia } = this.state;
    const denuncia_usuario = { latitude, longitude, denuncia };

    this.props.addDenunciaUsuario(denuncia_usuario);

    this.setState({
      latitude: "",
      longitude: "",
      denuncia: "",
      alreadyAdded: true
    });
  };

  render() {
    if (this.state.alreadyAdded) {
      return <Redirect to="/" />;
    }
    const { latitude, longitude, denuncia } = this.state;
    return (
      <div className="container">
        <Link to="/" className="btn btn-default">
          Voltar
        </Link>
        <div className="card card-body mt-4 mb-4">
          <h2>Adicionar Usuario Denuncia</h2>
          <form onSubmit={this.onSubmit}>
            <div className="form-group">
              <label>Latitude</label>
              <input
                className="form-control"
                type="text"
                name="latitude"
                onChange={this.onChange}
                value={latitude}
              />
            </div>
            <div className="form-group">
              <label>Longitude</label>
              <input
                className="form-control"
                type="text"
                name="longitude"
                onChange={this.onChange}
                value={longitude}
              />
            </div>
            <div className="form-group">
              <label>Categoria da Denuncia</label>
              <input
                className="form-control"
                type="number"
                name="denuncia"
                min="1"
                onChange={this.onChange}
                value={denuncia}
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
  { addDenunciaUsuario }
)(UsuarioDenunciaForm);
