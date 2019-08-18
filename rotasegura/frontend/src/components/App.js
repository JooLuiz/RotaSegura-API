import React, { Component, Fragment } from "react";
import ReactDOM from "react-dom";
import {
  HashRouter as Router,
  Route,
  Switch,
  Redirect
} from "react-router-dom";

import Header from "./layouts/Header";
import Alerts from "./layouts/Alerts";
import Login from "./accounts/Login";
import Register from "./accounts/Register";
import PrivateRoute from "./commom/PrivateRoute";
import Dashboard from "./rotasegura/Dashboard";
import TipoDenuncia from "./rotasegura/TipoDenuncia";
import Denuncia from "./rotasegura/Denuncia";
import UsuarioDenunciaForm from "./rotasegura/UsuarioDenunciaForm";

import { Provider as AlertProvider } from "react-alert";
import AlertTemplate from "react-alert-template-basic";

import { Provider } from "react-redux";
import store from "../store";
import { loadUser } from "../actions/auth";

//AlertOptions
const alertOptions = {
  timeout: 3000,
  position: "top center"
};

class App extends Component {
  componentDidMount() {
    store.dispatch(loadUser());
  }

  render() {
    return (
      <Provider store={store}>
        <AlertProvider template={AlertTemplate} {...alertOptions}>
          <Router>
            <Fragment>
              <Header />
              <Alerts />
              <div className="container">
                <Switch>
                  <PrivateRoute exact path="/" component={Dashboard} />
                  <Route exact path="/register" component={Register} />
                  <Route exact path="/login" component={Login} />
                  <Route
                    exact
                    path="/usuario_denuncia/new"
                    component={UsuarioDenunciaForm}
                  />
                  <Route exact path="/tipo_denuncia" component={TipoDenuncia} />
                  <Route exact path="/denuncia" component={Denuncia} />
                </Switch>
              </div>
            </Fragment>
          </Router>
        </AlertProvider>
      </Provider>
    );
  }
}

ReactDOM.render(<App />, document.getElementById("app"));
