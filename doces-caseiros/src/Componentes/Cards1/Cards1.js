import React, { useState } from "react";
import Button from "react-bootstrap/Button";
import Card from "react-bootstrap/Card";
import "./Cards1.css";

const Cards1 = () => {
  // Estado com os dados dos 4 Cards
  const [cards] = useState([
    {
      id: 1,
      title: "Doce de Leite",
      text: "O mais cremoso e saboroso, feito artesanalmente!",
      image: "/images/doce-leite.jpg",
      link: "/doce-leite",
    },
    {
      id: 2,
      title: "Brigadeiro Gourmet",
      text: "Um clássico brasileiro, agora mais sofisticado!",
      image: "/images/brigadeiro.jpg",
      link: "/brigadeiro",
    },
    {
      id: 3,
      title: "Pé de Moleque",
      text: "O crocante irresistível, direto da fazenda!",
      image: "/images/pe-moleque.jpg",
      link: "/pe-moleque",
    },
    {
      id: 4,
      title: "Bolo de Rolo",
      text: "Tradicional e delicioso, com camadas perfeitas!",
      image: "/images/bolo-rolo.jpg",
      link: "/bolo-de-rolo",
    },
  ]);

  return (  
    <div className="divpai-cards1">

      <div className="card-text">
          <h2>Nossos Doces</h2>  
      </div>

     {/* Renderização dos Cards */} 
      <div className="cards-container">
          {cards.map((card) => (
            <Card key={card.id} style={{ width: "18rem" }}>
              <Card.Img variant="top" src={card.image} alt={card.title} />
              <Card.Body>
                <Card.Title>{card.title}</Card.Title>
                <Card.Text>{card.text}</Card.Text>
                <Button variant="primary">Comprar</Button>
              </Card.Body>
            </Card>
          ))}
      </div> 

    </div>
  );
};

export default Cards1;
