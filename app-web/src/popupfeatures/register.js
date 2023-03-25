import React, { useState, useEffect } from "react";
import showIcon from '../assets/eye.png';
import hideIcon from '../assets/eye_open.png';
import bcrypt from 'bcryptjs';
import { v4 as uuidv4 } from 'uuid';
import CryptoJS from 'crypto-js'


export const Register = (props) => {
    const [showPopup, setShowPopup] = useState(true);
    const [showPassword, setShowPassword] = useState(false);
    const [username, setUsername] = useState('');
    const [id, setId] = useState('');
    const [APIkey, setApiKey] = useState('');
    const [APIpassword, setApiPassword] = useState('');
    const [APIsecret, setApiSecret] = useState('');
    const [password, setPassword] = useState('');
    const [rememberMe, setRememberMe] = useState(false);

  
    const secretKey = 'asdbchituenHGUBUYfdoznchioryoizf';
    

    const saltRounds = 10

    const handleSubmit = async (event) => {
        event.preventDefault();
        
            // Création d'un objet à partir des données saisies
          
        try {
          
        console.log(APIkey,APIsecret,APIpassword)
          const hashedPassword = await bcrypt.hash(password, saltRounds); 
          const encryptedAPIKey = CryptoJS.AES.encrypt(APIkey, secretKey).toString();
          const encryptedAPISecret = CryptoJS.AES.encrypt(APIsecret, secretKey).toString();
          const encryptedAPIPassword = CryptoJS.AES.encrypt(APIpassword, secretKey).toString();   
          console.log(encryptedAPIKey,encryptedAPISecret,encryptedAPIPassword)

          const data={
                      id: id,
                      password: hashedPassword, 
                      username: username,
                      APIkey: encryptedAPIKey,
                      APIsecret: encryptedAPISecret,
                      APIpassword: encryptedAPIPassword,
                      pairList :['BTC/USDT:USDT', 'ETH/USDT:USDT', 'BNB/USDT:USDT', 'XRP/USDT:USDT', 'ADA/USDT:USDT'],
                      maxActivePositions: 3,
                      running : true,
                      telegram: false,
                      chat_id: "NaN",
                      mode : 'automatic',
                      withMode: 'NaN' 
                      }
          
      
            const url = 'https://wklab094d7.execute-api.eu-west-1.amazonaws.com/items'
            const response = await fetch(url, {
              method: 'PUT',
              mode : 'cors',
              headers: {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json'
              },
              body: JSON.stringify(data)
            });

            if (response.ok) {
              document.cookie = `userId=${data.id}; maxAge: 30 * 24 * 60 * 60; path: '/'; /* httpOnly; */ secure`;
              setShowPopup(false);

              if (rememberMe) {
                const key = uuidv4();

                const cookieOptions = {
                  maxAge: 30 * 24 * 60 * 60, // Durée de validité de 30 jours
                  path: '/',
                };
                
                document.cookie = `sessionKey=${key}; ${cookieOptions}`;

            }} else {
              throw new Error('Une erreur s\'est produite.');
            }
          } catch (error) {
            console.error('Erreur:', error);
          }
        };
     
      const checkSession = async () => {
        const cookie = document.cookie.split('; ').find(row => row.startsWith('sessionKey='));
        if (cookie) {
        const sessionKey = cookie.split('=')[1];
        // Envoi de la requête POST au serveur pour vérifier la validité du cookie
        const url = `https://wklab094d7.execute-api.eu-west-1.amazonaws.com/items/${sessionKey}`
        const response = await fetch(url,{
            method: 'GET',
            mode : 'cors',
            headers: {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json'
            },
        });
        if (response.ok) {
            // Si le cookie est valide, l'utilisateur est authentifié automatiquement
            setShowPopup(false);
        } else {
            // Si le cookie n'est pas valide, le supprimer
            document.cookie = `sessionKey=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;`;
        }
        }
      };      
      
      useEffect(() => {
    
        checkSession();
    /*     const popupStateCookie = document.cookie.split(';').find(cookie => cookie.trim().startsWith('popupState='));
        if (popupStateCookie) {
          const popupState = popupStateCookie.split('=')[1];
          setShowPopup(popupState !== 'hidden');
        } */
      }, []);

      const togglePasswordVisibility = () => {
        setShowPassword(!showPassword);
      };

      
    const handleRememberMeChange = (e) => {
        setRememberMe(e.target.checked);
    };
      
    return (
         
        <>    
        {showPopup && <div onClick={() => setShowPopup(false)}></div>}
        {showPopup && (
        <div className="auth-form-container">
            <img className="imglogosimple" src={require("../assets/logo_simple.png")} alt="logo_simple_ava"/>
            <h3> Welcome to AVA Bot </h3>

            <form className="register-form" onSubmit={handleSubmit}>
                <div className="gaucheregister"> 
                    <label htmlFor="name">Username</label>
                    <input value={username} onChange={(e) => setUsername(e.target.value)} id="name" placeholder="your username" required />
                    <label htmlFor="email">Email</label>
                    <input value={id} onChange={(e) => setId(e.target.value)} type="email" placeholder="youremail@gmail.com" id="email" name="email" pattern="[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{1,63}$" required />
                    <label htmlFor="password">Password  <img className="password-icon" src={showPassword ? hideIcon : showIcon} alt={showPassword ? "Hide password" : "Show password"} onClick={togglePasswordVisibility}  /> </label> 
                    <input value={password} onChange={(e) => setPassword(e.target.value)} type={showPassword ? 'text' : 'password'} placeholder="your password" id="pass" name="pass"  pattern="(?=.*\d)(?=.*[A-Z])(?=.*[&(){}_-]).{5,}"  required title="Password must be at least 5 characters long and include at least one number, one uppercase letter, and one special character (&(){}_-)."/>
                    
                </div>
                <div className="droiteregister"> 
                    <label htmlFor="apiKey">API Key</label>
                    <input value={APIkey} onChange={(e) => setApiKey(e.target.value)} type="password" placeholder="your API Key" id="apiKey" name="apiKey" required />
                    <label htmlFor="apiPassword">API Password</label>
                    <input value={APIpassword} onChange={(e) => setApiPassword(e.target.value)} type="password" placeholder="your API Password" id="apiPassword" name="apiPassword" required />
                    <label htmlFor="apiSecret">API Secret</label>
                    <input value={APIsecret} onChange={(e) => setApiSecret(e.target.value)} type="password" placeholder="your API Secret" id="apiSecret" name="apiSecret" required/>
                </div>

                
                <button className="boutonlogin2"  type="submit">Create Account</button>
            </form>
            <label className="rememberme2" htmlFor="remember-me"><input type="checkbox" id="remember-me"  name="remember-me" checked={rememberMe} onChange={handleRememberMeChange} /> Remember me </label>
        <button className="link-btn2" onClick={() => props.onFormSwitch('login')}>Already have an account? Login here.</button>
    </div>
    )}
    </>
    )
}