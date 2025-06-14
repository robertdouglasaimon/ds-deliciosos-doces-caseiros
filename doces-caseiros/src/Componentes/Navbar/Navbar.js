import React from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import "./Navbar.css";
import logo from "../../Componentes/img/DS-SemFundo.png";

const Navbar = () => {
  return (
    <nav className="navbar navbar-expand-lg custom-navbar">
      <div className="container">
        {/* Logo da empresa */}
        <a href="#" className="navbar-brand">
          <img src={logo} alt="Logo Doces Caseiros" className="custom-logo" />
        </a>

        {/* Botão de menu responsivo */}
        <button className="navbar-toggler custom-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
          <span className="navbar-toggler-icon"></span>
        </button>

        {/* Links de navegação */}
        <div className="collapse navbar-collapse justify-content-center" id="navbarNav">
          <ul className="navbar-nav custom-nav">
            <li className="nav-item"><a className="nav-link custom-link" href="#">Início</a></li>
            <li className="nav-item"><a className="nav-link custom-link" href="#">Sobre</a></li>
            <li className="nav-item"><a className="nav-link custom-link" href="#">Contato</a></li>
          </ul>
        </div>

        {/* Botão de ação à direita */}
        <a className="btn custom-button" href="#">Administrador</a>
      </div>
    </nav>
  );
};

export default Navbar;
