import getCookie from "./features/getcookies"
import image1 from '../assets/logo_simple.png';
import "./styles/aboutyou.css"
import React, { useState, useEffect  } from 'react';
import Forgotpassword from '../popupfeatures/forgotpassword';
import CryptoJS from 'crypto-js';
import axios from "axios";


export default function Aboutyou() {
    const id = getCookie('userId');
    const [showPopup, setShowPopup] = useState(false); 
    const [chatid, setchatId] = useState('');
    const [data, setData] = useState([]);

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


        const secretKey = 'asdbchituenHGUBUYfdoznchioryoizf';
      
        
          
        

      /* 
        const decryptedAPIKey = CryptoJS.AES.decrypt(apiData.APIkey, secretKey).toString(CryptoJS.enc.Utf8);
        const decryptedAPISecret = CryptoJS.AES.decrypt(apiData.APIsecret, secretKey).toString(CryptoJS.enc.Utf8);
        const decryptedAPIPassword = CryptoJS.AES.decrypt(apiData.APIpassword, secretKey).toString(CryptoJS.enc.Utf8);
       */

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
                <h5 className="apiinfo">API Secret: {}</h5>
                <h5 className="apiinfo">API Key: {}</h5>
                <h5 className="apiinfo">API Password: {}</h5>
            </div>
            <div id="telegramaccount">
                <h3>Connect to Telegram?</h3>
                <label className="chatid"> Chat Id</label>
                <input value={chatid} onChange={(e) => setchatId(e.target.value)}  id="chatidtelegram" placeholder="you chat id" required/>
            </div>
        
            <button id="logoutaccount" onClick={handleLogout}>Log out</button>
                
            
        </div>
        </>
    )
}
