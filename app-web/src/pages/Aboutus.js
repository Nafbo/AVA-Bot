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
                  <p> In charge of the analysis of mathematical indicators and deployment of the application <br/> </p>
                </div>
                <div className="team-member">
                  <img src={require("../assets/alice_avatar.jpg")} />
                  <label className="team-member-name">Alice Miermon</label>
                  <br/>
                  <p> In charge of the serverless architecture et user experience / user interface design <br/> </p>
                </div>
                <div className="team-member">
                  <img src={require("../assets/adrian_avatar.jpg")}/>
                  <label className="team-member-name">Adrian Boyer</label>
                  <br/>
                  <p> In charge of the sentiment analysis and chatbot manager <br/><br/>  </p>
                </div>
                <div className="team-member">
                  <img src={require("../assets/victor_henrio_avatar.jpg")} />
                  <label className="team-member-name">Victor Henrio</label>
                  <br/>
                  <p> Supervisor of the project <br/><br/><br/><br/> </p>
                </div>
            </div>


            <div className="ava">

              <img src={require("../assets/logo_blanc.png")}/>
              <label> AVA Bot </label>
              <p> AVBot is an engineering end-of-studies project. The goal of this research project is to create a fully functional trading bot based on mathematical and sentimental analysis, with an ergonomic user interface that allows the user to see all information about the bot. This project uses AWS for the serverless architecture deployed fully on AWS (using API Gateway, Lambda Function, and DynamoDB Tables).
                <br/> <br/>  From the AVABot team, thanks for using our project! <br/> <br/> </p>
            </div>
          </div>
         
          <div className="bas-container"> 

            <div className="bitget-container">
              <img className="logo_img"src={require("../assets/bitget_logo.png")}/>
              <p> 
              Bitget is a cryptocurrency exchange platform that offers an API for developers to integrate the platform's functionalities into their applications and services. The BitGet API allows developers to create automated trading bots that can execute transactions at regular intervals based on predefined trading strategies. This can help users save time and maximize their profits. One of the other main advantages of Bitget is its advanced trading technology, which allows users to benefit from fast order execution, high liquidity, and enhanced security. Additionally, Bitget also offers a range of innovative trading products, such as futures trading, which enable users to maximize their profits using different leverage ratios. It is through this API that we open or close your positions, and with the API, you can also check your wallet funds on the application and monitor its real-time performance.
              <br/> <br/> Go to Bitget <a href="https://www.bitget.com/" target="_blank" rel="noopener noreferrer">https://www.bitget.com</a>.
              </p>
              <br/><br/><br/>
              
              
              <img className="exemple" src={require("../assets/bitget.png")}/>
              <br/> <br/> <br/> <br/>
              
              
             
              
            </div>
            <div className="telegram-container">
            <img className="logo_img2" src={require("../assets/telegram_logo.png")}/>
              <label>Telegram </label>
              <p> <br/>
              Telegram is a popular instant messaging application that allows users to communicate securely and quickly. The application is available on several platforms, including iOS, Android, Windows, Mac, and Linux.
              Using this application, we have created a messaging bot that will send pre-recorded messages to users on their phone, providing information about the position that the bot has opened or closed. To access this feature, our users simply need to log in to their Telegram account, so we can retrieve their "chat_id", which is the identifier for their Telegram account that allows us to send messages to their application.
              <br/> <br/> Go to Telegram <a href="https://telegram.org/" target="_blank" rel="noopener noreferrer">https://telegram.org</a>.
               </p>
               <br/>
              <img className="exemple2" src={require("../assets/telegram_message.png")}/>
            </div>

            
          </div>

       </div>
      
      
       
      )
  }