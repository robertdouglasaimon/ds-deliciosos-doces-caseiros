import React from "react";
import "./Banner.css";
import banner from "../../Componentes/img/banner.png";

const Banner = () => {
  return (
    <div className="banner">
      <img src={banner} alt="Banner Doces Artesanais" className="banner-image" title="Doces Artesanais"/>
      <div className="banner-content">
        {/* <h1>Doces Artesanais</h1> */}
        
          <p>
            Prove a doçura única de nossos doçes artesanais, feitos com <br/>
            ingredientes selecionados com muito amor.
          </p>
        
        <a href="#" className="btn btn-primary">Ver Produtos</a>
      </div>
    </div>
  );
};

export default Banner;
