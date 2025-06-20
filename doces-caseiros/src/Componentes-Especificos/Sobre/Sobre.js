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
                Me chamo Diego Santos, idealizador da DS Doces Artesanais. Nascido e criado em Pirassununga, interior de São Paulo, sempre fui fã da cozinha — aquele tipo de pessoa que come de tudo, que adora descobrir sabores. Depois que perdi meu pai, passei a viver com minha mãe e, entre altos e baixos, percebi que era hora de me jogar de cabeça naquilo que eu amava fazer: preparar doces.
            </p>
            <p>
                Não sou bom em escrever sobre mim, e minha vida é bem pacata. Mas gosto do meio-termo — nem lá, nem cá. Aquela ideia de vida justa, simples e tranquila. Pescar, dormir bem, comer direito, resolver as coisas de dentro pra fora... Isso me inspira tanto quanto as receitas que crio.
            </p>
            </div>
        </div>
    
        <div class="sobre1-container">
            <div className="sobre-texto1">
            <h2>História da empresa</h2>
            <p>
                 A DS Doces surgiu da vontade de oferecer doces menos prejudiciais, mais acessíveis e feitos com ingredientes reais. Nada de açúcar refinado quando dá pra usar mel. Nada de produto industrializado onde cabe um leite fresco de roça, um amendoim bem selecionado.
            </p>
            <p>
                A ideia foi simples desde o começo: fazer doces de qualidade, que qualquer pessoa pudesse consumir — inclusive quem tem restrições, como diabéticos. Comecei pequeno, trocando leite com um vizinho, ganhando açúcar de outro, e distribuindo os doces pra amigos da rua.
            </p>
            <p>
                Hoje o sonho é maior: levar sabor com consciência. Acreditamos que todo mundo merece comer bem — do rico ao mais simples. Que a alimentação também é parte do bem-estar. Nosso foco é servir com verdade, com carinho e com justiça.
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
