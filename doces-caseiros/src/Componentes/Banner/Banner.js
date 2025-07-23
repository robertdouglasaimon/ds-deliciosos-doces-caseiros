import React from "react";
import "./Banner.css";
import banner from "../../Componentes/img/banner.png";
import banner_sem_fundo from "../../Componentes/img/Sem fundo.png";
import { Link } from "react-router-dom";

const Banner = () => {
  return (
    <div className="banner">
      <img src={banner} alt="Banner Doces Artesanais" className="banner-image" title="Doces Artesanais"/>
      
      <div className="banner-content">
        {/* <h1>Doces Artesanais</h1> */}
        <p className="banner-text">
          Prove a doçura única de nossos doces artesanais, feitos com <br/>
          ingredientes selecionados com muito amor.
        </p>
        
        <Link to="/Produtos" className="btn btn-primary button-custom">Ver Produtos</Link>
      </div>
      
    </div>
  );
};

export default Banner;
