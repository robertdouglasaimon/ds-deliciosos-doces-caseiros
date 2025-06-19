import React from "react";
import "./Home.css";
import 'bootstrap/dist/css/bootstrap.min.css';
import Banner from "../../Componentes/Banner/Banner";
import Section1 from "../../Componentes/Section1/Section1";
import Section2 from "../../Componentes/Section2/Section2";
import Cards1 from  "../../Componentes/Cards1/Cards1";

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