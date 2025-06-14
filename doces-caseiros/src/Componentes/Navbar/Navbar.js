import React, { useState } from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import "./Navbar.css";
import logo from "../../Componentes/img/DS-SemFundo.png";

const Navbar = () => {
  const [isOpen, setIsOpen] = useState(false); // Estado inicial do menu (fechado)

  return (
    <nav className="navbar navbar-expand-lg custom-navbar">
      <div className="container">
        {/* Logo da empresa */}
        <a href="#" className="navbar-brand">
          <img src={logo} alt="Logo Doces Caseiros" className="custom-logo" />
        </a>

        {/* Botão de menu hamburguer */}
        <button className="navbar-toggler custom-toggler" type="button" onClick={() => setIsOpen(!isOpen)}>
          <span className="navbar-toggler-icon"></span>
        </button>

        {/* Links de navegação */}
        <div className={`collapse navbar-collapse ${isOpen ? "show" : ""}`} id="navbarNav">
          <ul className="navbar-nav custom-nav">
            <li className="nav-item"><a className="nav-link custom-link" href="#">Início</a></li>
            <li className="nav-item"><a className="nav-link custom-link" href="#">Sobre</a></li>
            <li className="nav-item"><a className="nav-link custom-link" href="#">Contato</a></li>
            {/* Botão Administrador dentro do menu hamburguer */}
            <li className="nav-item d-lg-none"><a className="btn btn-admin" href="#">Administrador</a></li>
          </ul>
        </div>

        {/* Botão Administrador visível só em telas grandes */}
        <a className="btn btn-admin d-none d-lg-block" href="#">Administrador</a>
      </div>
    </nav>
  );
};

export default Navbar;
