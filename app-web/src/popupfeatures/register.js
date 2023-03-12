import React, { useState } from "react";
import showIcon from '../assets/eye.png';
import hideIcon from '../assets/eye_open.png';
import bcrypt from 'bcryptjs';


export const Register = (props) => {
    const [showPopup, setShowPopup] = useState(true);
    const [showPassword, setShowPassword] = useState(false);
    const [username, setUsername] = useState('');
    const [id, setId] = useState('');
    const [APIkey, setApiKey] = useState('');
    const [APIpassword, setApiPassword] = useState('');
    const [APIsecret, setApiSecret] = useState('');
    const [password, setPassword] = useState('');



    const saltRounds = 10


    const togglePasswordVisibility = () => {
      setShowPassword(!showPassword);
    };
    const handleSubmit = async (event) => {
        event.preventDefault();
        
/*         // Vérifier que tous les champs sont remplis
      /*   if (/* !username || */ /* !id /* || !image */ /* || !APIkey || !APIpassword || !APIsecret || !password) { */ 
            /* alert('Veuillez remplir tous les champs');
            return;
        } */ 
    
        // Vérifier que l'email est valide
/*         const idRegex = /\S+@\S+\.\S+/;
        if (!idRegex.test(id)) {
            alert('Veuillez entrer une adresse e-mail valide');
            return;
        } */
    
        // Vérifier que le mot de passe a au moins 8 caractères
/*         if (password.length < 5) {
            alert('Le mot de passe doit avoir au moins 5 caractères');
            return;
        } */
    
            // Création d'un objet à partir des données saisies
          
        try {
          const hashedPassword = await bcrypt.hash(password, saltRounds);    
          const data={
                      id: id,
                      password: hashedPassword, 
                      username: username,
                      APIkey: APIkey,
                      APIsecret: APIsecret,
                      APIpassword: APIpassword,
                      pairList :"Nan",
                      maxActivePositions: "Nan",
                      running : "NaN"
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
              setShowPopup(false);
            } else {
              throw new Error('Une erreur s\'est produite.');
            }
          } catch (error) {
            console.error('Erreur:', error);
          }
/*             .then(response => {
              if (response.ok) {
                return response.json();
              } else {
                throw new Error('Une erreur s\'est produite.');
              }
            })
            .then(data => {
              console.log(data); 
              setShowPopup(false);
            })
            .catch(error => {
              console.error('Erreur:', error);
            }); */
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
                    <input value={password} onChange={(e) => setPassword(e.target.value)} type={showPassword ? 'text' : 'password'} placeholder="your password" id="pass" name="pass" pattern="(?=.*[A-Z])(?=.*[!@#$&*])(?=.*[a-z])(?=.*\d).{5,}" required title="at least 5 characters and one number, including one uppercase letter and one special character"/>
                    
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
        <button className="link-btn2" onClick={() => props.onFormSwitch('login')}>Already have an account? Login here.</button>
    </div>
    )}
    </>
    )
}