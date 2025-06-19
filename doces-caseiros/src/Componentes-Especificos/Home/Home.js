import React from "react";
import "./Home.css";
import 'bootstrap/dist/css/bootstrap.min.css';
import Banner from '../../Componentes/Banner/Banner';
import Section1 from '../Home/Section1/Section1';
import Section2 from '../Home/Section2/Section2';
import Cards1 from '../Home/Cards1/Cards1';


const Home = () => {
    return (
        <div className="home">
            <header>
                <Banner />
            </header>
            <main>
                <Cards1 />
                <Section1 />
                <Section2 />
            </main>
        </div>
    );
};

export default Home;