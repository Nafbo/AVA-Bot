import React, { useState, useEffect } from "react";
import showIcon from '../assets/eye.png';
import hideIcon from '../assets/eye_open.png';
import bcrypt from 'bcryptjs';
import { v4 as uuidv4 } from 'uuid';

export const Login = (props) => {
    const [showPopup, setShowPopup] = useState(true);
    const [showPassword, setShowPassword] = useState(false);
    const [id, setId] = useState('');
    const [password, setPassword] = useState('');
    
    
    const [rememberMe, setRememberMe] = useState(false);
    /* const key = uuidv4(); */
    /* document.cookie = "sessionKey=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;"; */
    const handleSubmit = async (e) => {
      e.preventDefault();
  
      try {
          // Envoi de la requête POST au serveur
          const url = `https://wklab094d7.execute-api.eu-west-1.amazonaws.com/items/${id}`
          const response = await fetch(url,{
              method: 'GET',
              mode : 'cors',
              headers: {
                  'Access-Control-Allow-Origin': '*',
                  'Content-Type': 'application/json'
              },
          });
          
          if (!response.ok) {
              throw new Error('An error occurred while fetching user data.');
          }
  
          const data = await response.json();
          if (data) {
              const storedPassword = data[0].password;
              const passwordMatch = await bcrypt.compare(password, storedPassword);
              console.log(passwordMatch)
              if (passwordMatch) {
                  console.log('Utilisateur connecté');
                  document.cookie = `userId=${data[0].id}; maxAge: 30 * 24 * 60 * 60; path: '/'; /* httpOnly; */ secure`;
                  setShowPopup(false);

                   // Création du cookie si "Remember Me" est coché
                   if (rememberMe) {
                    const key = uuidv4();

                    const cookieOptions = {
                      maxAge: 30 * 24 * 60 * 60, // Durée de validité de 30 jours
                      path: '/',
                    };
                    
                    document.cookie = `sessionKey=${key}; ${cookieOptions}; /* httpOnly; */ secure`;
                    
                    

                   /*  // Stockage de l'état du popup dans le cookie
                    document.cookie = `popupState=hidden; ${cookieOptions}`; */

              } 
            } else {
                  throw new Error('Wrong username or password');
              }
          } else {
              throw new Error("User doesn't exist");
          }
  
      } catch (error) {
          // Gestion des erreurs
          console.error(error);
          alert(error.message);
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
            /* const user = await response.json();
            setId(user.id); */
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

      const handleForgotPassword = () => {
        props.onFormSwitch('forgotpassword');
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
                <form className="login-form" onSubmit={handleSubmit}>
                    <label htmlFor="email">Your Email</label>
                    <input value={id} onChange={(e) =>{ console.log('Email changed to:', e.target.value); setId(e.target.value)} }type="email" placeholder="youremail@gmail.com" id="email" name="email" />
                    <label htmlFor="password"> Your Password  <img className="password-icon" src={showPassword ? hideIcon : showIcon} alt={showPassword ? "Hide password" : "Show password"} onClick={togglePasswordVisibility}  /> </label> 
                    <input value={password} onChange={(e) => {console.log('Password changed to:', e.target.value); setPassword(e.target.value)}} type={showPassword ? 'text' : 'password'} placeholder="your password" id="pass" name="pass" required />
                    <button className="link-btnpassword" onClick={handleForgotPassword}> forgot your password? Click Here </button>
                    <button className="boutonlogin" type="submit">Log In</button>
                    <label className="rememberme" htmlFor="remember-me"><input type="checkbox" id="remember-me"  name="remember-me" checked={rememberMe} onChange={handleRememberMeChange} /> Remember me </label>
                </form>
                <button className="link-btn" onClick={() => props.onFormSwitch('register')}>Don't have an account? Register here.</button>
            </div>
            )}
        </>
    )
}

//AliceTest456&