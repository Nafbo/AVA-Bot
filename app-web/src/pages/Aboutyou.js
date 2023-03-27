import getCookie from "./features/getcookies"
import image1 from '../assets/logo_simple.png';
import "./styles/aboutyou.css"
import React, { useState, useEffect  } from 'react';
import Forgotpassword from '../popupfeatures/forgotpassword';
import CryptoJS from 'crypto-js';
import axios from "axios";


export default function Aboutyou() {

    useEffect(() => {
      document.title = "AVABot Account"; 
    }, []);
  
    const id = getCookie('userId');
    const [showPopup, setShowPopup] = useState(false); 
    const [chatid, setchatId] = useState('');
    const [apiKeyValue, setapiKeyValue] = useState('');
    const [apiPassvalue, setapiPassvalue] = useState('');
    const [apiSecretValue, setapiSecretValue] = useState('');

    const handleLogout = () => {
        document.cookie = "sessionKey=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
        // rediriger l'utilisateur vers la page de connexion après la déconnexion
        window.location.href = '/';
      };

      const fetchData = async () => {
        try {
          const id = getCookie('userId');
          console.log( id );
          const response = await axios.get(`https://ttwjs0n6o1.execute-api.eu-west-1.amazonaws.com/items/${id}`);
          console.log(response.data)
          console.log(response.status) // should be 200 for a successful request
        console.log(response.headers) // should contain any relevant headers from the API response
          // Utilisez ces valeurs pour mettre à jour l'état de votre composant, si nécessaire.
        } catch (error) {
          console.error(error);
        }
      };
      
      useEffect(() => {
        fetchData();
      }, []);
      


    const datatel = { 
        telegram : chatid
      }
    
      const url = `https://wklab094d7.execute-api.eu-west-1.amazonaws.com/items/${id}`
      fetch(url, {
        method: 'PATCH',
        mode : 'cors',
        headers: {
          'Access-Control-Allow-Origin': '*',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(datatel)
      }).then(() => {
          console.log(datatel)
        });


      
      const hideandshowsecret = () => {
        var x = document.getElementById("divhideapisecret");
        const manualButton = document.querySelector(".manuel");
        if (x.style.display === "none") {
          x.style.display = "block";
          manualButton.classList.add("active");
        } else {
          x.style.display = "none";
          manualButton.classList.remove("active");
        }
      } 
      
      const hideandshowkey = () => {
        var x = document.getElementById("divhideapikey");
        const manualButton = document.querySelector(".manuel");
        if (x.style.display === "none") {
          x.style.display = "block";
          manualButton.classList.add("active");
        } else {
          x.style.display = "none";
          manualButton.classList.remove("active");
        }
      }  

      const hideandshowpass = () => {
        var x = document.getElementById("divhideapipassword");
        const manualButton = document.querySelector(".manuel");
        if (x.style.display === "none") {
          x.style.display = "block";
          manualButton.classList.add("active");
        } else {
          x.style.display = "none";
          manualButton.classList.remove("active");
        }
      }  

  // ----------------------------------------

  const updateApiSecret=(apiSecretValue)=> {
    const secretKey = 'asdbchituenHGUBUYfdoznchioryoizf';
    const requestData = {
      method: 'PATCH',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ APIsecret: CryptoJS.AES.encrypt(apiSecretValue, secretKey).toString() })
    };
  
    const id = getCookie('userId');
    fetch(`https://wklab094d7.execute-api.eu-west-1.amazonaws.com/items/${id}`, requestData)
      .then(response => {
        if (!response.ok) {
          throw new Error('Error updating API Secret');
        }
        return response.json();
      })
      .then(data => {
        console.log('API Secret updated successfully:');
      })
      .catch(error => {
        console.error(error);
      });
  }
   
  
  
    const updateApiKey = (apiKeyValue) => {
      const secretKey = 'asdbchituenHGUBUYfdoznchioryoizf';
      const requestData = {
        method: 'PATCH',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ APIkey: CryptoJS.AES.encrypt(apiKeyValue, secretKey).toString() })
      };
      const id = getCookie('userId');
      fetch(`https://wklab094d7.execute-api.eu-west-1.amazonaws.com/items/${id}`, requestData)
        .then(response => {
          if (!response.ok) {
            throw new Error('Error updating API Key');
          }
          return response.json();
        })
        .then(data => {
          console.log('API Key updated successfully:');
        })
        .catch(error => {
          console.error(error);
        });
    }
    
    
    const updateApiPassword = (apiPassvalue) =>{
      const secretKey = 'asdbchituenHGUBUYfdoznchioryoizf';
      const requestData = {
        method: 'PATCH',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ APIpassword: CryptoJS.AES.encrypt(apiPassvalue, secretKey).toString() })
      };
      const id = getCookie('userId');
      fetch(`https://wklab094d7.execute-api.eu-west-1.amazonaws.com/items/${id}`, requestData)
        .then(response => {
          if (!response.ok) {
            throw new Error('Error updating API Password');
          }
          return response.json();
        })
        .then(data => {
          console.log('API Password updated successfully:');
        })
        .catch(error => {
          console.error(error);
        });
    }



    return (  
        <> 
        
        {showPopup && (
        <div className="popup-pass">
            <Forgotpassword onClose={() => setShowPopup(false)} />
            <p onClick={() => setShowPopup(false)}> close </p>
        </div>
        )}

        <div className="account" >
            
            <img id="logoava" src={image1}  alt="ava logo"/>     
            
            
            <h1 id="titleaccount">Welcome to your account</h1>
            <div id='idaccount' >
                <h3>Your id</h3>
                <p>{id}</p>
                <label>change your password ? <button className="changepass" onClick={() => setShowPopup(true)}> click here </button></label>
            </div>
          
            <div id="apiaccount">
                <h3>Your API</h3>
                <label>API Secret: <button className={ 'manual' ? 'active' : ''} onClick={hideandshowsecret}> click here </button></label>
                <label>API Key: <button className={'manual' ? 'active' : ''} onClick={hideandshowkey}> click here </button></label>
                <label>API Password: <button className={'manual' ? 'active' : ''} onClick={hideandshowpass}> click here </button></label>

                <div id="divhideapisecret" style = {{display:"none"}}>
                  <input defaultValue={apiSecretValue}  id="apisecret" placeholder="you API Secret" required/> <button className="buttonsecret" onClick={() => updateApiSecret(document.querySelector("#apisecret").value)}> ok </button>
                </div>

                <div id="divhideapikey" style = {{display:"none"}}>
                  <input defaultValue={apiPassvalue}  id="apikey" placeholder="you API Key" required/> <button className="buttonkey" onClick={() => updateApiKey(document.querySelector("#apikey").value)}> ok </button>
                </div>

                <div id="divhideapipassword" style = {{display:"none"}}>
                  <input defaultValue={apiKeyValue} id="apipassword" placeholder="you API password" required/> <button className="buttonpassword" onClick={() => updateApiPassword(document.querySelector("#apipassword").value)}> ok </button>
                </div>
            </div>
            <div id="telegramaccount">
                <h3>Connect to Telegram?</h3>
                <label className="chatid"> Chat Id <span className="info-icon" title="See on About Us page how to get your chat_id for Telegram"></span></label>
                <input value={chatid} onChange={(e) => setchatId(e.target.value)}  id="chatidtelegram" placeholder="you chat id" required/>
            </div>
        
            <button id="logoutaccount" onClick={handleLogout}>Log out</button>
                
            
        </div>
        </>
    )
}
