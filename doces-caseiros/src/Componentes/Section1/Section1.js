import React from "react";
import "./Section1.css";
import d1 from "../../Componentes/Section1/img-slide/d1.png";
import d2 from "../../Componentes/Section1/img-slide/d2.png";
import d3 from "../../Componentes/Section1/img-slide/d3.png";
import d4 from "../../Componentes/Section1/img-slide/d4.png";
import d5 from "../../Componentes/Section1/img-slide/d5.png";
import { Row, Col, Carousel } from "react-bootstrap";


const Section1 = () => {
  return (
    <div>
    <section className="section1 neon-container">
        <div className="container">
            <Row className="align-items-center">
            <Col md={6}>

            {/* Carrossel de imagens */}
            <div className="carousel-wrapper">
            <Carousel fade interval={3500}>
            <Carousel.Item>
                <img className="d-block w-100" src={d4} alt="Preparo artesanal no tacho" />
                <Carousel.Caption>
                <h3>Sabor que nasce no tacho</h3>
                <div class="estilizacao-descricao-slide">
                    <p>
                        Doces preparados à mão, no fogão a lenha, com ingredientes
                        frescos e tradição em cada colherada.
                    </p>
                </div>
                </Carousel.Caption>
            </Carousel.Item>

            <Carousel.Item>
                <img className="d-block w-100" src={d1} alt="Fogão à lenha DS Doces" />
                <Carousel.Caption>
                <h3>Tradição em fogo brando</h3>
                <div class="estilizacao-descricao-slide">
                    <p>
                        Nos bastidores do sabor, a lenha esquenta receitas que atravessam gerações.
                    </p>
                </div>
                </Carousel.Caption>
            </Carousel.Item>

            <Carousel.Item>
                <img className="d-block w-100" src={d2} alt="Entregador com caixa DS" />
                <Carousel.Caption>
                <h3>Do nosso tacho pra sua casa</h3>
                <div class="estilizacao-descricao-slide">
                    <p>
                        Entregamos com simpatia e qualidade. O doce chega até você com carinho.
                    </p>
                </div>
                </Carousel.Caption>
            </Carousel.Item>

            <Carousel.Item>
                <img className="d-block w-100" src={d5} alt="Cocada de Coco Queimado" />
                <Carousel.Caption>
                <h3>Cocada de Coco Queimado</h3>
                <div class="estilizacao-descricao-slide">
                    <p>
                        Feita com coco fresco e aquele toque caramelizado irresistível.
                    </p>
                </div>
                </Carousel.Caption>
            </Carousel.Item>

            <Carousel.Item>
                <img className="d-block w-100" src={d3} alt="Marca DS Doces na mesa" />
                <Carousel.Caption>
                <h3>DS Doces Artesanais</h3>
                <div class="estilizacao-descricao-slide">
                    <p>
                        Mais que sabor — é identidade, afeto e experiência feita à mão pra você.
                    </p>
                </div>
                </Carousel.Caption>
            </Carousel.Item>
            </Carousel>
            </div>

            </Col>
            <Col md={6}>
                <div className="section1-texto">
                <h2>A Magia dos Doces Artesanais</h2>
                <p>
                    Na DS Doces, cada detalhe importa. 
                    Do fogão a lenha ao cuidado com a entrega, nossos doces 
                    são mais do que receitas: são presentes que carregam afeto, sabor 
                    e aquele toque especial que transforma o dia.
                </p>
                <p>
                    Nosso compromisso é com a qualidade, o frescor e o prazer de surpreender 
                    quem recebe — seja com uma cocada dourada ou um gesto simples de carinho.
                </p>
                </div>
            </Col>
            </Row>
        </div>
    </section>



    </div>
  );
};

export default Section1;
