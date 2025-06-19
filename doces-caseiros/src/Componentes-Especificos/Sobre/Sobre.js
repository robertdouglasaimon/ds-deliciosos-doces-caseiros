import "./Sobre.css";
import Diego1 from './img-sobre/Diego1.png';
import doces1 from './img-sobre/doces1.png';
const Sobre = () => {
  return (
    <div className="sobre">
        <div className="sobre-container">
            <div className="sobre-img neon-border">
            <img
                src={Diego1}
                alt="Fundador da DS Doces Artesanais"
            />
            </div>

            <div className="sobre-texto">
            <h2>Sobre Mim</h2>
            <p>
                Sou [Nome do Fundador], idealizador da DS Doces Artesanais. Apaixonado por sabores que
                aquecem a alma, transformei a tradição familiar em negócio — com receitas que fazem parte da minha história.
            </p>
            <p>
                Cada doce é feito com carinho, ingredientes selecionados e aquele cuidado de quem valoriza o artesanal. Obrigado por fazer parte dessa jornada doce com a gente!
            </p>
            </div>
        </div>
    
        <div class="sobre1-container">
            <div className="sobre-texto1">
            <h2>História da empresa</h2>
            <p>
                Sempre gostei de cozinha. Desde novo, via na comida uma forma de cuidar, de expressar carinho — e foi nela que encontrei força pra recomeçar.
            </p>
            <p>
                 Moro em Pirassununga, interior de São Paulo. Após perder meu pai, minha mãe e eu tivemos que nos virar pra seguir em frente. Foi aí que resolvi apostar de verdade no que sempre me trouxe conforto: fazer doce.
            </p>
            <p>
                Comecei pequeno, sem certeza de nada, mas com muita vontade. E graças a cada pessoa que acreditou, a coisa tá dando certo. Agora, meu sonho é crescer, levar os sabores que preparo com tanto carinho pra mais lugares — e seguir adoçando a vida de quem me dá essa chance. <br/>
                Obrigado por fazer parte disso.
            </p>

            {/* <div className="redes-sociais">
                <a href="https://wa.me/5519991750239" target="_blank" rel="noreferrer">
                <img src="https://cdn-icons-png.flaticon.com/512/733/733585.png" alt="WhatsApp" />
                </a>
                <a href="https://www.instagram.com/ds_doces_artesanais?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==" target="_blank" rel="noreferrer">
                <img src="https://cdn-icons-png.flaticon.com/512/1384/1384063.png" alt="Instagram" />
                </a>
            </div> */}
            </div> 

            <div className="sobre-img1 neon-border">
            <img
                src={doces1}
                alt="Fundador da DS Doces Artesanais"
            />
            </div>       
        </div>

    </div>
  );
};

export default Sobre;
