import React, { useState } from "react";
import { Link } from 'react-router-dom';
import "bootstrap/dist/css/bootstrap.min.css";
import "./Navbar.css";
import logo from "../../Componentes/img/DS-SemFundo.png";


const Navbar = () => {
  const [isOpen, setIsOpen] = useState(false); // Estado inicial do menu (fechado)

  return (
    <nav className="navbar navbar-expand-lg custom-navbar">
      <div className="container">
        {/* Logo da empresa */}
        <Link className="navbar-brand" to="/Home">
          <img src={logo} alt="Logo Doces Caseiros" className="custom-logo" />
        </Link>

        {/* Botão de menu hamburguer */}
        <button className="navbar-toggler custom-toggler" type="button" onClick={() => setIsOpen(!isOpen)}>
          <span className="navbar-toggler-icon"></span>
        </button>

        {/* Links de navegação */}
        <div className={`collapse navbar-collapse ${isOpen ? "show" : ""}`} id="navbarNav">
          <ul className="navbar-nav custom-nav">
            <li className="nav-item"><Link className="nav-link custom-link" to="/Home">Início</Link></li>
            <li className="nav-item"><Link className="nav-link custom-link" to="/Sobre">Sobre</Link></li>
            <li className="nav-item"><Link className="nav-link custom-link" to="/Produtos">Produtos</Link></li>
            <li className="nav-item"><Link className="nav-link custom-link" to="/Contato">Contato</Link></li>
            {/* Botão Administrador dentro do menu hamburguer */}
            <li className="nav-item d-lg-none">
            <a className="btn btn-admin" href="https://sistema-controle-ds-doces-caseiros.streamlit.app/" target="_blank" rel="noopener noreferrer">Administrador</a>
            </li>
          </ul>
        </div>

        {/* Botão Administrador visível só em telas grandes */}
        <a className="btn btn-admin d-none d-lg-block" href="https://sistema-controle-ds-doces-caseiros.streamlit.app/" target="_blank" rel="noopener noreferrer">
          Administrador
        </a>

      </div>
    </nav>
  );
};

export default Navbar;
