import React, { useState, useEffect } from "react";
import showIcon from '../assets/eye.png';
import hideIcon from '../assets/eye_open.png';
import bcrypt from 'bcryptjs';

export const Login = (props) => {
    const [showPopup, setShowPopup] = useState(true);
    const [showPassword, setShowPassword] = useState(false);
    const [id, setId] = useState('');
    const [password, setPassword] = useState('');
    const [rememberMe, setRememberMe] = useState(false);



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
         console.log(data)
         console.log("longueur", data.lenght>0)
          if (data) {
            console.log(data)
            console.log(data[0])
            console.log(data[0].password)
            console.log(password)
              const storedPassword = data[0].password;
              const passwordMatch = await bcrypt.compare(password, storedPassword);
              console.log(passwordMatch)
              if (passwordMatch) {
                  console.log('Utilisateur connecté');
                  setShowPopup(false);
              } else {
                  throw new Error('Wrong username or password');
              }
          } else {
              throw new Error("User doesn't exist");
          }
  
          /* if (rememberMe) {
              setCookie('loggedIn', 'true', 7); // Cookie expires in 7 days
          } */
      } catch (error) {
          // Gestion des erreurs
          console.error(error);
          alert(error.message);
      }
  };

      const togglePasswordVisibility = () => {
        setShowPassword(!showPassword);
      };

      const handleForgotPassword = () => {
        props.onFormSwitch('forgotpassword');
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
                </form>
                <button className="link-btn" onClick={() => props.onFormSwitch('register')}>Don't have an account? Register here.</button>
            </div>
            )}
        </>
    )
}