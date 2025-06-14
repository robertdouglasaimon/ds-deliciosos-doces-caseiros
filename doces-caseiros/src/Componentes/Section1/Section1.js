import React from "react";
import "./Section1.css"; // Arquivo de estilos
import slide1 from '../../Componentes/Section1/img-slide/cocada-de-coco-queimado.png';
import slide2 from '../../Componentes/Section1/img-slide/diego-1.png';
import slide3 from '../../Componentes/Section1/img-slide/DS.png';
import { Carousel } from "react-bootstrap";

const Section1 = () => {
  return (
    <div>
        <section className="section1">
            <h2>Sobre Nossos Doces</h2>
            <p>Prove a doçura única de nossos doces artesanais!</p>
        </section> 

        {/* Carousel de imagens*/}
        <div className="carousel">
            <Carousel>
                <Carousel.Item>
                <img src={slide1} text="Primeiro Slide" />
                    <Carousel.Caption>
                        <h3>First slide label</h3>
                        <p>Nulla vitae elit libero, a pharetra augue mollis interdum.</p>
                    </Carousel.Caption>
                </Carousel.Item>

               <Carousel.Item>
               <img src={slide2} text="Segundo Slide" />
                    <Carousel.Caption>
                        <h3>Second slide label</h3>
                        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
                    </Carousel.Caption>
                </Carousel.Item>
                 
                <Carousel.Item>
                <img src={slide3} text="Terceiro Slide" />
                    <Carousel.Caption>
                        <h3>Third slide label</h3>
                        <p>Praesent commodo cursus magna, vel scelerisque nisl consectetur.</p>
                    </Carousel.Caption>
                </Carousel.Item>

                 {/* <Carousel.Item>
                    <ExampleCarouselImage text="Third slide" />
                    <Carousel.Caption>
                    <h3>Third slide label</h3>
                    <p>
                        Praesent commodo cursus magna, vel scelerisque nisl consectetur.
                    </p>
                    </Carousel.Caption>
                </Carousel.Item> */}

            </Carousel>
        </div>
    </div>
  );
};

export default Section1;