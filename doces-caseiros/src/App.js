import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './Componentes/Navbar/Navbar';
import Footer from './Componentes/Footer/Footer';
import Home from './Componentes-Home/Home/Home';

function App() {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/Home" element={<Home />} />
        <Route path="/Produtos" element={<h1>Página em construção...</h1>} />
        <Route path="/Sobre" element={<h1>Página em construção...</h1>} />
        <Route path="/Contato" element={<h1>Página em construção...</h1>} />
      </Routes>
      <Footer />
    </Router>
  );
}

export default App;
