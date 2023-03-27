import React, { useEffect, useState, useMemo } from "react";
import "./styles/aboutus.css"
export default function Aboutus() {

  useEffect(() => {
    document.title = "AVABot About Us"; 
  }, []);

    return (
      
        <div className="tout">
          
          <div className="haut-container"> 
            <div className="team-ava-container">
              
                <div className="team-member">
                  <img src={require("../assets/victor_avatar.jpg")} />
                  <label className="team-member-name">Victor Bonnafous</label>
                  <br/>
                  <p> In charge of the analysis of mathematical indicators and deployment of the application</p>
                </div>
                <div className="team-member">
                  <img src={require("../assets/alice_avatar.jpg")} />
                  <label className="team-member-name">Alice Miermon</label>
                  <br/>
                  <p> Responsable architecture serverless et user experience / user interface design</p>
                </div>
                <div className="team-member">
                  <img src={require("../assets/adrian_avatar.jpg")}/>
                  <label className="team-member-name">Adrian Boyer</label>
                  <br/>
                  <p> Responsable for sentiment analysis and chatbot manager</p>
                </div>
                <div className="team-member">
                  <img src={require("../assets/victor_henrio_avatar.jpg")} />
                  <label className="team-member-name">Victor Henrio</label>
                  <br/>
                  <p> Supervisor of the project</p>
                </div>
            </div>


            <div className="ava">

                  <img src={require("../assets/logo_simple.png")}  />

            </div>
          </div>
         
          <div className="bas-container"> 

            <div className="bitget-container">
              <p>
                Bitget est une plateforme d'échange de crypto-monnaies qui propose une API pour permettre aux développeurs d'intégrer les fonctionnalités de la plateforme dans leurs applications et leurs services. L'API de BitGet permet aux développeurs de créer des bots de trading automatisés qui peuvent exécuter des transactions à des intervalles réguliers en fonction de stratégies de trading prédéfinies. Cela peut permettre aux utilisateurs de gagner du temps et de maximiser leurs profits.L'un des autres principaux avantages de Bitget est sa technologie de trading avancée, qui permet aux utilisateurs de bénéficier d'une exécution rapide des ordres, d'une liquidité élevée et d'une sécurité renforcée. En outre, Bitget propose également une gamme de produits de trading innovants, tels que le trading de futur, qui permettent aux utilisateurs de maximiser leurs profits en utilisant différents leviers. C’est donc grâce à cette API que nous ouvrons ou fermons vos positions, grâce à l’api, vous pouvez aussi connaître les fonds de votre portefeuille sur l’application et suivre en direct son évolution.
                <a href="https://www.bitget.com/" target="_blank" rel="noopener noreferrer">https://www.bitget.com</a>.
              </p>
            </div>
            <div className="telegram-container">
              <p>
                Telegram est une plateforme d'échange de crypto-monnaies qui propose une API pour permettre aux développeurs d'intégrer les fonctionnalités de la plateforme dans leurs applications et leurs services. L'API de BitGet permet aux développeurs de créer des bots de trading automatisés qui peuvent exécuter des transactions à des intervalles réguliers en fonction de stratégies de trading prédéfinies. Cela peut permettre aux utilisateurs de gagner du temps et de maximiser leurs profits.L'un des autres principaux avantages de Bitget est sa technologie de trading avancée, qui permet aux utilisateurs de bénéficier d'une exécution rapide des ordres, d'une liquidité élevée et d'une sécurité renforcée. En outre, Bitget propose également une gamme de produits de trading innovants, tels que le trading de futur, qui permettent aux utilisateurs de maximiser leurs profits en utilisant différents leviers. C’est donc grâce à cette API que nous ouvrons ou fermons vos positions, grâce à l’api, vous pouvez aussi connaître les fonds de votre portefeuille sur l’application et suivre en direct son évolution.
                <a href="https://telegram.org/" target="_blank" rel="noopener noreferrer">https://telegram.org</a>.
              </p>
            </div>

            
          </div>

       </div>
      
      
       
      )
  }