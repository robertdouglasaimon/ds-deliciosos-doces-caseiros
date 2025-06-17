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
        {/* <Route path="/sobre" element={<Sobre />} /> */}
        {/* <Route path="/contato" element={<Contato />} /> */}
      </Routes>
      <Footer />
    </Router>
  );
}

export default App;
