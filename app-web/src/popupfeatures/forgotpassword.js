import React, { useState, useEffect } from "react";
import axios from "axios";
import bcrypt from 'bcryptjs';

import showIcon from '../assets/eye.png';
import hideIcon from '../assets/eye_open.png';

export const Forgotpassword = (props) => {
  const [id, setId] = useState("");
  const [item, setItem] = useState(null);
  const [tokenSent, setTokenSent] = useState(false);
  const [/* token */, setToken] = useState("");
  const [password, setPassword] = useState("");
  const [passwordConfirmed, setPasswordConfirmed] = useState("");
  const [resetSuccess, setResetSuccess] = useState(false);
  const [showPassword, setShowPassword] = useState(false);

  const saltRounds = 10

  const togglePasswordVisibility = () => {
      setShowPassword(!showPassword);
  };

  const handleSubmitEmail = (e) => {
    e.preventDefault();
    axios
      .get(`https://wklab094d7.execute-api.eu-west-1.amazonaws.com/items/${id}`)
      .then((response) => {
        if (response.data.length > 0) {
          setItem(response.data[0]);
          setTokenSent(true);
          // Envoi du jeton par e-mail à l'utilisateur
        } else {
          alert("L'adresse e-mail saisie n'existe pas dans notre système.");
        }
      });
  };

  useEffect(() => {
    // Vérifier si l'utilisateur a déjà un jeton enregistré dans l'URL
    const urlParams = new URLSearchParams(window.location.search);
    const token = urlParams.get("token");
    if (token) {
      setToken(token);
      setTokenSent(true);
    }
  }, []);

  const handleSubmitPassword = async (e) => {
    e.preventDefault();
    const hashedPassword = await bcrypt.hash(password, saltRounds);    
    const passwordMatch = await bcrypt.compare(password, item.password);
    if (passwordMatch) {
      // Le nouveau mot de passe est identique au mot de passe actuel
      alert("Le nouveau mot de passe doit être différent de l'ancien mot de passe.");
      return;
    }
  
    const data = { 
      password: hashedPassword 
    }
  
    const url = `https://wklab094d7.execute-api.eu-west-1.amazonaws.com/items/${id}`
    console.log(url)
    console.log(data)
    console.log(id)
    fetch(url, {
      method: 'PATCH',
      mode : 'cors',
      headers: {
        'Access-Control-Allow-Origin': '*',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    }).then(() => {
        console.log(data)
        setResetSuccess(true);
      });
  
  } 

  if (resetSuccess) {
    return (
      <> 
    <div className="auth-form-container">
      <img className="imglogosimple" src={require("../assets/logo_simple.png")} alt="logo_simple_ava"/>
      <h5 className="title3"> Your password has been reset with success </h5>
      <button className="boutonlogin" onClick={() => props.onFormSwitch('login')}> Return to Login </button>
    </div> 
    </>)
  } 
  else if (tokenSent) {
    return (
      <div className="auth-form-container"> 
        <img className="imglogosimple" src={require("../assets/logo_simple.png")} alt="logo_simple_ava"/>
        <h3> Reset your password </h3>
        <form className="login-form" onSubmit={handleSubmitPassword}>
          <label> Create a new password <img className="password-icon" src={showPassword ? hideIcon : showIcon} alt={showPassword ? "Hide password" : "Show password"} onClick={togglePasswordVisibility} /> </label> 
          <input value={password} onChange={(e) => setPassword(e.target.value)} type={showPassword ? 'text' : 'password'} placeholder="new password" id="pass" name="pass" pattern="(?=.*\d)(?=.*[A-Z])(?=.*[&(){}_-]).{5,}"  required title="Password must be at least 5 characters long and include at least one number, one uppercase letter, and one special character (&(){}_-)." />
          
          <label> Confirmed the new password <img className="password-icon" src={showPassword ? hideIcon : showIcon} alt={showPassword ? "Hide password" : "Show password"} onClick={togglePasswordVisibility}/> </label>
          <input value={passwordConfirmed} onChange={(e) => setPasswordConfirmed(e.target.value)} type={showPassword ? 'text' : 'password'} placeholder="confirmed password" id="pass" name="pass"  pattern="(?=.*\d)(?=.*[A-Z])(?=.*[&(){}_-]).{5,}"  required />
          
          <button className="boutonlogin" type="submit"  disabled={password !== passwordConfirmed}> Réinitialiser le mot de passe </button>
        </form>
      </div>
    );
  } else {
    return (
      <div className="auth-form-container"> 
        <img className="imglogosimple" src={require("../assets/logo_simple.png")} alt="logo_simple_ava"/>
        <h3> Reset your password </h3>
        <form className="login-form" onSubmit={handleSubmitEmail}>
          <label htmlFor="email"> Your email  </label>
          <input type="email" value={id} onChange={(e) => setId(e.target.value)} placeholder="your email" required/>
          <button className="boutonlogin" type="submit"> Réinitialiser le mot de passe </button>
        </form>
        <button className="link-btnretour" onClick={() => props.onFormSwitch('login')}>return</button>
      </div>
    );
  }
};

export default Forgotpassword;
