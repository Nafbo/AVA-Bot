import React, { useState } from "react";
import './popup.css';
import { Login } from "./login";
import { Register } from "./register";
import { Forgotpassword } from "./forgotpassword";

function Popup() {
  const [currentForm, setCurrentForm] = useState('login');

  const toggleForm = (formName) => {
    setCurrentForm(formName);
  }

  return (
    <div className="Popup">
      {currentForm === "login" ? (
        <Login onFormSwitch={toggleForm} />
      ) : currentForm === "register" ? (
        <Register onFormSwitch={toggleForm} />
      ) : (
        <Forgotpassword onFormSwitch={toggleForm} />
      )}
    </div>
  );
}

export default Popup;