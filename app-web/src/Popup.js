import React, { useState } from 'react';
import axios from 'axios';
import robot1 from './assets/robot1.png';
import robot2 from './assets/robot2.png';
import robot3 from './assets/robot3.png';
import robot4 from './assets/robot4.png';

export default function Popup(){
  const [showPopup, setShowPopup] = useState(true);
/*   const [username, setUsername] = useState(''); */
  const [id, setId] = useState('');
 /*  const [image, setImage] = useState(''); */
  const [APIkey, setApiKey] = useState('');
  const [APIpassword, setApiPassword] = useState('');
  const [APIsecret, setApiSecret] = useState('');
  const [password, setPassword] = useState(''); 
/*   const [pairList, setPairList] = useState('');
  const [maxActivePositions, setMaxActivePositions] = useState('');
  const [running, setRunning] = useState(''); */


  const handleSubmit = (event) => {
    event.preventDefault();
    
    /* // Vérifier que tous les champs sont remplis
    if (!username || !id || !image || !apiKey || !apiPassword || !apiSecret || !password) {
        alert('Veuillez remplir tous les champs');
        return;
    }

    // Vérifier que l'email est valide
    const idRegex = /\S+@\S+\.\S+/;
    if (!idRegex.test(id)) {
        alert('Veuillez entrer une adresse e-mail valide');
        return;
    }

    // Vérifier que le mot de passe a au moins 8 caractères
    if (password.length < 5) {
        alert('Le mot de passe doit avoir au moins 5 caractères');
        return;
    } */

        // Création d'un objet à partir des données saisies
    const data = {
        id: id,
        password: password, 
       /*  username: username, */
/*         image: image, */
         APIkey: APIkey,
        APIsecret: APIsecret,
        APIpassword: APIpassword,
        pairList :"Nan",
        maxActivePositions: "Nan",
        running : "NaN"
        };

      const url = 'https://wklab094d7.execute-api.eu-west-1.amazonaws.com/items'
      fetch(url, {
        method: 'PUT',
        mode : 'cors',
        headers: {
          'Access-Control-Allow-Origin': '*',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
      })
      .then(response => {
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
      });
    }
   

    return (
    <>
      {showPopup && <div className="overlay" onClick={() => setShowPopup(false)}></div>}
      {showPopup && (
          <div className="popup">
            <form onSubmit={handleSubmit}>
              <h2>Création de compte / Connexion</h2> */
  {/*             <div className="form-group">
                <label htmlFor="username">Nom d'utilisateur</label>
                <input type="text" id="username" value={username} onChange={(e) => setUsername(e.target.value)} required />
              </div> */}
              <div className="form-group">
                <label htmlFor="email">Email</label>
                <input type="email" id="email" value={id} onChange={(e) => setId(e.target.value)} required />
              </div>
  {/*             <div className="form-group">
                <label htmlFor="image">Image</label>
                <select id="image" value={image} onChange={(e) => setImage(e.target.value)}>
                  <option value="">Choisissez une image</option>
                  <option value="robot1" src={robot1}/>
                  <option value="robot2" src={robot2}/>
                  <option value="robot3" src={robot3}/>
                  <option value="robot4" src={robot4}/>
                </select>
              </div> */}
              <div className="form-group">
                <label htmlFor="apiKey">API Key</label>
                <input type="password" id="apiKey" value={APIkey} onChange={(e) => setApiKey(e.target.value)} required />
              </div>
              <div className="form-group">
                <label htmlFor="apiPassword">API Password</label>
                <input type="password" id="apiPassword" value={APIpassword} onChange={(e) => setApiPassword(e.target.value)} required />
              </div>
              <div className="form-group">
                <label htmlFor="apiSecret">API Secret</label>
                <input type="password" id="apiSecret" value={APIsecret} onChange={(e) => setApiSecret(e.target.value)} required />
              </div>
              <div className="form-group">
                <label htmlFor="password">Mot de passe</label>
                <input type="password" id="password" value={password} onChange={(e) => setPassword(e.target.value)} required />
              </div>
              <button type="submit">Valider</button>
            </form>
          </div>
        )}
      </>
  )
} 