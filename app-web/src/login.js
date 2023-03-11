import React, { useState, useEffect } from "react";
import showIcon from './assets/eye.png';
import hideIcon from './assets/eye_open.png';

export const Login = (props) => {
    const [showPopup, setShowPopup] = useState(true);
    const [showPassword, setShowPassword] = useState(false);
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [rememberMe, setRememberMe] = useState(false);

/*     useEffect(() => {
        const emailCookie = getCookie('email');
        const passwordCookie = getCookie('password');
    
        if (emailCookie && passwordCookie) {
          setEmail(emailCookie);
          setPassword(passwordCookie);
          setRememberMe(true);
        }
      }, []); */

    const getCookie = (name) => {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) {
        return parts.pop().split(';').shift();
    }
    };
    
    // Function to set the value of a cookie
    const setCookie = (name, value, days) => {
    let expires = "";
    if (days) {
        const date = new Date();
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
        expires = `; expires=${date.toUTCString()}`;
    }
    document.cookie = `${name}=${value || ""}${expires}; path=/`;
    };
    
    // Function to delete a cookie
    const deleteCookie = (name) => {
    document.cookie = `${name}=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;`;
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        
        // Envoi de la requête POST au serveur
        const url = 'https://wklab094d7.execute-api.eu-west-1.amazonaws.com/items'
        fetch(url, {
            method: 'PUT',
            mode : 'cors',
            headers: {
              'Access-Control-Allow-Origin': '*',
              'Content-Type': 'application/json'
            },
          body: JSON.stringify({
            email: email,
            password: password
          })
        })
        .then(response => response.json())
        .then(data => {
            console.log(data); 
            setShowPopup(false);

            if (rememberMe) {
                setCookie('loggedIn', 'true', 7); // Cookie expires in 7 days
              }
          })
        .catch(error => {
          // Gestion des erreurs
          console.error(error);
          alert('An error occurred while logging in. Please try again later.');
        });
      };

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
                <img className="imglogosimple" src={require("./assets/logo_simple.png")} alt="logo_simple_ava"/>
                <h3> Welcome to AVA Bot </h3>
                <form className="login-form" onSubmit={handleSubmit}>
                    <label htmlFor="email">Your Email</label>
                    <input value={email} onChange={(e) => setEmail(e.target.value)}type="email" placeholder="youremail@gmail.com" id="email" name="email" />
                    <label htmlFor="password"> Your Password  <img className="password-icon" src={showPassword ? hideIcon : showIcon} alt={showPassword ? "Hide password" : "Show password"} onClick={togglePasswordVisibility}  /> </label> 
                    <input value={password} onChange={(e) => setPassword(e.target.value)} type={showPassword ? 'text' : 'password'} placeholder="your password" id="pass" name="pass" required />
                    <div> <input type="checkbox" id="remember-me" name="remember-me" checked={rememberMe} onChange={handleRememberMeChange} /> <label className="rmberme" htmlFor="remember-me"> Remember me</label></div>
                    
                    
                    <button className="boutonlogin" type="submit">Log In</button>
                </form>
                <button className="link-btn" onClick={() => props.onFormSwitch('register')}>Don't have an account? Register here.</button>
            </div>
            )}
        </>
    )
}