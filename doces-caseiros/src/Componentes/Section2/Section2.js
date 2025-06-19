import React, { useState } from "react";
import "./Section2.css";
import { Modal, Row, Col } from "react-bootstrap";
import depoimento1 from "../../Componentes/Section2/img-depoimentos/depoimento1.jpg";
import depoimento2 from "../../Componentes/Section2/img-depoimentos/depoimento2.jpg";
import depoimento3 from "../../Componentes/Section2/img-depoimentos/depoimento3.jpg";

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
