import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import Navbar from './Componentes/Navbar/Navbar';
import Banner from './Componentes/Banner/Banner';
import Footer from './Componentes/Footer/Footer';
import Cards1 from './Componentes/Cards1/Cards1';
import Section1 from './Componentes/Section1/Section1';
import Section2 from './Componentes/Section2/Section2';

function App() {
  return (
    <div className="App">
        <header>
          <Navbar />
          <Banner />
        </header>
        <main>
            <Cards1 />
            <Section1 />
            <Section2 />
        </main>
        <footer>
          <Footer />
        </footer>
    </div>
  );
}

export default App;
