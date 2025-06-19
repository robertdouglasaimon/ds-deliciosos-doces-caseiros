import "./Contato.css";
import modelo1 from './contato-img/modelo1.png';

const Contato = () => {
  return (
    <div className="contato">
      <div className="contato-container">
        <div className="contato-texto">
          <h2>Fale com a Gente</h2>
          <p>
            Para encomendas, dúvidas ou apenas um oi: estamos a um clique de distância!  
            Entre em contato pelo WhatsApp ou acompanhe nosso dia a dia no Instagram.  
            Será um prazer adoçar o seu momento.
          </p>

          <div className="contato-icones">
            <a href="https://wa.me/5519991750239" target="_blank" rel="noreferrer">
              <img src="https://cdn-icons-png.flaticon.com/512/733/733585.png" alt="WhatsApp" />
            </a>
            <a href="https://www.instagram.com/ds_doces_artesanais?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==" target="_blank" rel="noreferrer">
              <img src="https://cdn-icons-png.flaticon.com/512/1384/1384063.png" alt="Instagram" />
            </a>
          </div>
        </div>

        <div class="espacamento-foto">
            <div className="contato-img neon-border">
              <img
                src={modelo1}
                alt="Foto de Contato"
              />
            </div>
        </div>
      </div>
    </div>
  );
};

export default Contato;
