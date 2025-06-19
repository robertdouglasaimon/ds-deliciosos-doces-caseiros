import React, { useState } from "react";
import "./Section2.css";
import { Modal, Row, Col } from "react-bootstrap";
import depoimento1 from "../../Home/Section2/img-depoimentos/depoimento1.jpg";
import depoimento2 from "../../Home/Section2/img-depoimentos/depoimento2.jpg";
import depoimento3 from "../../Home/Section2/img-depoimentos/depoimento3.jpg";
import depoimento4 from "../../Home/Section2/img-depoimentos/depoimento4.jpg";
import depoimento5 from "../../Home/Section2/img-depoimentos/depoimento5.jpg";
import depoimento6 from "../../Home/Section2/img-depoimentos/depoimento6.png";
import depoimento7 from "../../Home/Section2/img-depoimentos/depoimento7.png";
import depoimento8 from "../../Home/Section2/img-depoimentos/depoimento8.png";
import depoimento9 from "../../Home/Section2/img-depoimentos/depoimento9.png";


// Mock de depoimentos
const depoimentos = [
  {
    nome: "Lê Lelds",
    cidade: "Pirassununga - SP",
    fala: "Gente do céu, comprei esse doce do meu amigo Diego. Misericórdia 😍 é divino 🥰 ",
    foto: depoimento1,
  },
  {
    nome: "@drireginanasc",
    cidade: "Pirassununga - SP",
    fala: "Se você é fã de Ambrosia não deixe de provar. É boa demais 🧡💛",
    foto: depoimento2,
  },
  {
    nome: "Renata",
    cidade: "Pirassununga - SP",
    fala: "Gratidão 😋😋😍",
    foto: depoimento3,
  },
  {
    nome: "Samia Keller",
    cidade: "Pirassununga - SP",
    fala: "Esse é o doce de leite caseiro feito pelo @ds_doces_artesanais que eu utilizo nos muffins sabor doce de leite.",
    foto: depoimento4,
  },
  {
    nome: "Rodolfo Molina",
    cidade: "Bocaina - SP",
    fala: "Parabéns pela qualidade e pelo sabor maravilhoso.",
    foto: depoimento5,
  },
  {
    nome: "João",
    cidade: "Mogi Mirim - SP",
    fala: "Entregas especiais!",
    foto: depoimento6,
  },
  {
    nome: "Renata",
    cidade: "Pirassununga - SP",
    fala: "Hoje foi dia de experimentar o arroz doce com doce de leite que delicia ☺️😋😍",
    foto: depoimento7,
  },
  {
    nome: "Marina",
    cidade: "Pirassununga - SP",
    fala: "Doce maravilhoso!",
    foto: depoimento8,
  },
  {
    nome: "Renata",
    cidade: "Pirassununga - SP",
    fala: "Quase que não deu tempo para a foto.",
    foto: depoimento9,
  },
];

const Section2 = () => {
  const [show, setShow] = useState(false);
  const [selecionado, setSelecionado] = useState(null);

  const abrirModal = (item) => {
    setSelecionado(item);
    setShow(true);
  };

  const fecharModal = () => {
    setShow(false);
    setSelecionado(null);
  };

  return (
    <div className="section2">
      <h2 className="depoimentos-titulo">Depoimentos</h2>
      <p className="depoimentos-intro">
        Quem prova, aprova — e ainda faz questão de compartilhar. 💛 <br/>
        Veja o que alguns clientes disseram após experimentar os sabores que carregam histórias e tradição em cada colherada.
      </p>

      <div className="cartas-depoimentos">
        {depoimentos.map((item, index) => (
          <div key={index} className="card-depoimento" onClick={() => abrirModal(item)}>
            <img src={item.foto} alt={item.nome} className="foto-card" />
            <p className="nome-cliente">{item.nome}</p>
          </div>
        ))}
      </div>

      <Modal show={show} onHide={fecharModal} centered>
        {selecionado && (
          <Modal.Body>
            <Row className="popup-depoimento">
              <Col md={5}>
                <img src={selecionado.foto} alt={selecionado.nome} className="foto-popup" />
              </Col>
              <Col md={7}>
                <h4>{selecionado.nome}</h4>
                <small className="cidade-popup">{selecionado.cidade}</small>
                <p className="fala-popup">"{selecionado.fala}"</p>
              </Col>
            </Row>
          </Modal.Body>
        )}
      </Modal>
    </div>
  );
};

export default Section2;
