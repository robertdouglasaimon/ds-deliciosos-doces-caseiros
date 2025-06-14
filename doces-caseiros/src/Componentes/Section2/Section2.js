import Card from 'react-bootstrap/Card';
import depoimento1 from '../../Componentes/Section2/img-depoimentos/depoimento1.png';
import "./Section2.css";


const Section2 = () => {
  return (
    <div className="section2">
      <div class="depoimentos-text">            
        <h2>Depoimentos</h2>
      </div>
      
      <div class="card-depoimento">
        <Card>
          {/* <Card.Header>Quote</Card.Header> */}
          <Card.Body>
            <blockquote className="blockquote mb-0">
              <p>
                <img src={depoimento1} alt="icone-depoimento" className="foto-depoimento" />
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer
                posuere erat a ante.
              </p>
              <footer className="blockquote-footer">
                Someone famous in <cite title="Source Title">Source Title</cite>
              </footer>
            </blockquote>
          </Card.Body>
        </Card>
      </div>
    </div>
  );
}

export default Section2;
