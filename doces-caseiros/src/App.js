import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './Componentes/Navbar/Navbar';
import Footer from './Componentes/Footer/Footer';
import Home from './Componentes-Especificos/Home/Home';
import Produtos from './Componentes-Especificos/Produtos/Produtos';
import Sobre from './Componentes-Especificos/Sobre/Sobre';
import Contato from './Componentes-Especificos/Contato/Contato';

function App() {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/Home" element={<Home />} />
        <Route path="/Sobre" element={<Sobre />} />
        <Route path="/Produtos" element={<Produtos />} />
        <Route path="/Contato" element={<Contato />} />
      </Routes>
      <Footer />
    </Router>
  );
}

export default App;
