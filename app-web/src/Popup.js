import React, { useState } from "react";
import logo from './assets/avalogo.png';
import './popup.css';
import { Login } from "./login";
import { Register } from "./register";

function Popup() {
  const [currentForm, setCurrentForm] = useState('login');

  const toggleForm = (formName) => {
    setCurrentForm(formName);
  }

  return (
    <div className="Popup">
      {
        currentForm === "login" ? <Login onFormSwitch={toggleForm} /> : <Register onFormSwitch={toggleForm} />
      }
    </div>
  );
}

export default Popup;