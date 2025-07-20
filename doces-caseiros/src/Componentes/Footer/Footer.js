import React from "react";
import "./Footer.css";

const Footer = () => {
  // Função para atualizar o ano automaticamente.
  const year = new Date().getFullYear();

  return (
    <footer className="custom-footer">
        <p>
            <b>© {year} <a href="https://www.instagram.com/ds_doces_artesanais?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==">DS Doces Artesanais Caseiros</a>. CNPJ:59.900.451/0001-28.<br/> Todos os direitos reservados.</b>
            <b> Desenvolvido por <a href="https://github.com/robertdouglasaimon">Robert Douglas</a></b>
        </p>
    </footer>
  );
};

export default Footer;
