import React, { useState } from "react";
import "./Produtos.css";
import { Modal, Button, Form, Card } from "react-bootstrap";
import { useEffect } from "react";

import produto1 from './img-produtos/produto1.jpg';
import produto2 from './img-produtos/produto2.jpg';
import produto3 from './img-produtos/produto3.jpg';
import produto4 from './img-produtos/produto4.jpg';
import produto5 from './img-produtos/produto5.jpg';
import produto6 from './img-produtos/produto6.jpg';
import produto7 from './img-produtos/produto7.jpg';
import produto8 from './img-produtos/produto8.jpg';
import produto9 from './img-produtos/produto9.jpg';
import produto10 from './img-produtos/produto10.jpg';


const produtos = [
  {
    id: 1,
    nome: "Doce de Abóbora",
    descricao: "Com cravo e canela para um sabor rústico e marcante.",
    composicao: "Abóbora madura, açúcar cristal, cravo e canela. 600g. ",
    preco: "R$ 15,00",
    imagem: produto1,
  },
  {
    id: 2,
    nome: "Ambrosia Zero Lactose",
    descricao: "Versão sem lactose desse clássico afetivo.",
    composicao: "Leite zero lactose, açúcar cristal, ovos, cravo, canela e limão. 600g",
    preco: "R$ 19,00",
    imagem: produto2,
  },
  {
    id: 3,
    nome: "Arroz Doce com Doce de Leite",
    descricao: "Aquele arroz doce cremoso com toque de doce de leite.",
    composicao: "Leite de sítio, doce de leite, arroz tipo 1 e açúcar cristal. 600g",
    preco: "R$ 15,00",
    imagem: produto3,
  },
  {
    id: 4,
    nome: "Ambrosia",
    descricao: "Aquele sabor tradicional, agora acessível para quem busca uma opção sem lactose.",
    composicao: "Leite de sítio, açúcar cristal, ovos, cravo, canela e limão. 600g",
    preco: "R$ 17,00",
    imagem: produto4,
  },
  {
    id: 5,
    nome: "Doce de Leite",
    descricao: "Feito com leite de sítio, mel e um pouco de sal.",
    composicao: "Leite de sítio, açúcar cristal, mel e sal.",
    preco: "R$ 17,00",
    imagem: produto5,
  },
  {
    id: 6,
    nome: "Arroz Doce com Doce de Leite Zero Lactose",
    descricao: "Feito com leite zero lactose, doce de leite zero lactose, arroz tipo 1 e açúcar cristal.",
    composicao: "Leite zero lactose, doce de leite zero lactose, arroz tipo 1 e açúcar cristal. 600g",
    preco: "R$ 17,00",
    imagem: produto6,
  },
  {
    id: 7,
    nome: "Doce de Leite Zero Lactose", 
    descricao: "Feito com leite zero lactose, açucar cristal, mel e um pouco de sal.",
    composicao: "Leite zero lactose, açúcar cristal, mel e sal.",
    preco: "R$ 19,00",
    imagem: produto7,
  },
  {
    id: 8,
    nome: "Pasta de Amendoim Tradicional Integral",
    descricao: "Feito com 100% amendoim integral!",
    composicao: "Amendoim 100% integral levemente torrado. 170g",
    preco: "R$ 12,00",
    imagem: produto8,
  },    
  {
    id: 9,
    nome: "Pasta de Amendoim Paçoca",
    descricao: "Amendoim levemente torrado.",
    composicao: "Amendoim levemente torrado, mel e um pouco de sal. 170g",
    preco: "R$ 14,00",
    imagem: produto9,
  },
  {
    id: 10,
    nome: "Pasta de Amendoim Alcalina",
    descricao: "Amendoim levemente torrado.",
    composicao: "100% cacau, mel e um pouco de sal. 170g",
    preco: "R$ 16,00",
    imagem: produto10,
  },
  // Adicione o restante dos produtos aqui da mesma forma
];

const Produtos = () => {
  const [showInfo, setShowInfo] = useState(false);
  const [showCompra, setShowCompra] = useState(false);
  const [produtoSelecionado, setProdutoSelecionado] = useState(null);
  const [formData, setFormData] = useState({
    nome: "",
    endereco: "",
    telefone: "",
    quantidade: "",
    precisaTroco: "nao",
    valorTroco: "",
  });

  const abrirInfo = (produto) => {
    setProdutoSelecionado(produto);
    setShowInfo(true);
  };

  const abrirCompra = (produto) => {
    setProdutoSelecionado(produto);
    setShowCompra(true);
  };

  const fecharModais = () => {
    setShowInfo(false);
    setShowCompra(false);
    setProdutoSelecionado(null);
    setFormData({
      nome: "",
      endereco: "",
      telefone: "",
      quantidade: "",
      precisaTroco: "nao",
      valorTroco: "",
    });
  };

  const handleInput = (e) => {
    const { name, value } = e.target;
    setFormData((dados) => ({ ...dados, [name]: value }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    const mensagem = `COMPRA DIRECIONADA DO SITE DS DOCES ARTESANAIS
Cliente: ${formData.nome}
Endereço: ${formData.endereco}
Telefone: ${formData.telefone}
Produto: ${produtoSelecionado?.nome}
Quantidade: ${formData.quantidade}
Valor a ser trocado: ${
      formData.precisaTroco === "sim"
        ? formData.valorTroco || "Valor não especificado"
        : "Não é necessário troco!"
    }

Confirmar compra?
Nota: Em caso de desistência, por favor notifique neste contato.`;

    const encodedMessage = encodeURIComponent(mensagem);
    const numeroWhatsApp = "5519991750239";
    window.open(`https://wa.me/${numeroWhatsApp}?text=${encodedMessage}`, "_blank");
    fecharModais();
  };
  
  {/*Quando os botões de redirecionamento lá em baixo dos cards feitos em Cards1 forem apertado, ele direcionar suavemente usando esse useEffect. Para não dar aquele efeito abrupto de subir a página loucamente.*/}
  useEffect(() => {
    const hash = window.location.hash;
    if (hash) {
      const el = document.getElementById(hash.substring(1));
      if (el) {
        el.scrollIntoView({ behavior: "smooth", block: "start" });
      }
    }
  }, []);
  

  return (
    <div className="produtos">
      <h2 className="titulo-produtos">Produtos</h2>
      <p className="intro-produtos">
        Conheça nossa linha de produtos artesanais preparados com ingredientes selecionados, tradição e carinho.
        Cada potinho aqui tem história, sabor e afeto — escolha o seu favorito e leve um pedacinho do doce feito à mão pra sua casa!
      </p>

      <div className="produtos-grid">
        {produtos.map((item, index) => (
          <Card key={item.id} className="produto-card" id={item.id.toString()}>
            <Card.Img variant="top" src={item.imagem} />
            <Card.Body>
              <Card.Title>{item.nome}</Card.Title>
              <Card.Text>{item.descricao}</Card.Text>
              <p className="preco">{item.preco}</p>
              <div className="botoes">
                <Button size="sm" onClick={() => abrirInfo(item)} variant="info">
                  Saiba mais
                </Button>{" "}
                <Button size="sm" onClick={() => abrirCompra(item)} variant="success">
                  Compre aqui
                </Button>
              </div>
            </Card.Body>
          </Card>
        ))}
      </div>

      {/* Modal Saiba Mais */}
      <Modal show={showInfo} onHide={fecharModais} centered>
        <Modal.Header closeButton>
          <Modal.Title>{produtoSelecionado?.nome}</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <img src={produtoSelecionado?.imagem} alt={produtoSelecionado?.nome} className="imagem-modal" />
          <p><strong>Composição:</strong> {produtoSelecionado?.composicao}</p>
        </Modal.Body>
      </Modal>

      {/* Modal Compra */}
      <Modal show={showCompra} onHide={fecharModais} centered>
        <Modal.Header closeButton>
          <Modal.Title>Comprar: {produtoSelecionado?.nome}</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <Form onSubmit={handleSubmit}>
            <Form.Group>
              <Form.Label>Nome</Form.Label>
              <Form.Control name="nome" required onChange={handleInput} />
            </Form.Group>
            <Form.Group>
              <Form.Label>Endereço</Form.Label>
              <Form.Control name="endereco" required onChange={handleInput} />
            </Form.Group>
            <Form.Group>
              <Form.Label>Telefone</Form.Label>
              <Form.Control name="telefone" required onChange={handleInput} />
            </Form.Group>
            <Form.Group>
              <Form.Label>Quantidade</Form.Label>
              <Form.Control name="quantidade" required onChange={handleInput} />
            </Form.Group>
            <Form.Group>
              <Form.Label>Precisa de troco?</Form.Label>
              <Form.Select name="precisaTroco" onChange={handleInput}>
                <option value="nao">Não</option>
                <option value="sim">Sim</option>
              </Form.Select>
            </Form.Group>
            {formData.precisaTroco === "sim" && (
              <Form.Group>
                <Form.Label>Para qual valor?</Form.Label>
                <Form.Control name="valorTroco" onChange={handleInput} />
              </Form.Group>
            )}
            <Button type="submit" className="btn-whats" variant="success" block>
              Enviar para WhatsApp
            </Button>
          </Form>
        </Modal.Body>
      </Modal>
    </div>
  );
};

export default Produtos;
