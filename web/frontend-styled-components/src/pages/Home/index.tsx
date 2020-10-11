import React from 'react'
import { FcCurrencyExchange, FcFolder, FcOpenedFolder } from "react-icons/fc";
import { Link } from "react-router-dom"

import './index.css'


function Home() {

    return (
        <div className="field-group">
            <div className="field">
                <Link to="/vendas">
                    <FcCurrencyExchange size={250}/>
                    <span>Efetuar Vendas</span>
                </Link>
            </div>

            <div className="field">
            <Link to="/cadastro-produto">
                <FcFolder size={250} />
                <span>Cadastrar Produto</span>
            </Link>   
            </div>

            <div className="field">
                <Link to="/estoque">
                    <FcOpenedFolder size={250} />
                    <span>Verificar Estoque Atual</span>
                </Link>
                
            </div>

        </div>
        
    )
  }
  
  export default Home;
  