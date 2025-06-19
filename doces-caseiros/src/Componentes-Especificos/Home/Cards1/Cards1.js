import React, { useState } from "react";
import { Link } from "react-router-dom";
import Button from "react-bootstrap/Button";
import Card from "react-bootstrap/Card";
import "./Cards1.css";
import foto1 from "./img-doces/1.jpg";
import foto2 from "./img-doces/2.jpg";
import foto3 from "./img-doces/3.jpg";
import foto4 from "./img-doces/4.jpg";


const Cards1 = () => {
  // Estado com os dados dos 4 Cards
  const [cards] = useState([
    {
      title: "Doce de Abobora",
      text: "Um doce artesanal, feito com ingredientes selecionados como: abóbora madura, açucar cristalizado, cravo e canela. Trazendo um sabor autêntico e irresistível! Perfeito para quem aprecia qualidade e tradição!",
      image: foto1,
      link: "1",
    },
    {
      title: "Ambrosia Zero Lactose",
      text: "Uma ambrosia artesanal e irresistível, feita com leite zero lactose, açúcar cristal, ovos, cravo, canela e um toque especial de limão. Todo o sabor tradicional, agora acessível para quem busca uma opção sem lactose!",
      image: foto2,
      link: "2",
    },
    {
      title: "Arroz Doce com Doce de Leite",
      text: "O equilíbrio perfeito entre cremosidade e tradição! Nosso arroz doce especial é feito com leite de sítio, doce de leite artesanal, arroz tipo 1 e açúcar cristal. Cada colherada traz um sabor aconchegante e irresistível!",
      image: foto3,
      link: "3",
    },
    {
      title: "Ambrosia",
      text: "Uma ambrosia cremosa e artesanal, feita com leite de sítio, açúcar cristal, ovos, cravo, canela e limão. Cada colherada traz o sabor inconfundível de uma receita tradicional, preparada com carinho para momentos especiais!",
      image: foto4,
      link: "4",
    },
  ]);

  return (  
    <div className="divpai-cards1">

      <div className="card-text">
          <h2>Sabores Que Encantam!</h2> 
          <p>Na DS Doces Artesanais, cada receita é preparada com carinho, <br/>
          tradição e ingredientes cuidadosamente selecionados. Nossos doces combinam <br/>
          sabor e qualidade para proporcionar momentos especiais. Descubra nossas <br/>
          delícias e saiba mais sobre o que torna cada doce único!</p> 
      </div>

     {/* Renderização dos Cards */} 
      <div className="cards-container">
          {cards.map((card) => (
            <Card key={card.id} style={{ width: "18rem" }}>
              <Card.Img variant="top" src={card.image} alt={card.title} />
              <Card.Body>
                <Card.Title className="titulo-do-card">{card.title}</Card.Title>
                <Card.Text>{card.text}</Card.Text>
                <Link to={`/Produtos#${card.link}`}>
                  <Button variant="primary" className="button-custom">
                      <Button variant="primary" className="button-custom">Saiba Mais</Button> 
                  </Button>
                </Link>
              </Card.Body>
            </Card>
          ))}
      </div> 

    </div>
  );
};

export default Cards1;
