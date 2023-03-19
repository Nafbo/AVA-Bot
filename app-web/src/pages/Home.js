
import { Carousel } from 'react-bootstrap';
import image1 from '../assets/robot1.png';
import image2 from '../assets/robot2.png';
import image3 from '../assets/robot3.png';
import image4 from '../assets/robot4.png';
import 'bootstrap/dist/css/bootstrap.min.css';
import "./styles/home.css"
import getCookie from "./features/getcookies"
import React, { useState, useEffect } from "react"; 

export default function Home() {

  const userId = getCookie('userId');

  

    return(
    
    <div className='home'> 
      
      <div id="gauche">
        <img src={image1} id="robot1" alt="robot 1"/>     
      </div>

      <div className='droite'> 
      <div id='Title'>
        <h1> Your AVA Bot</h1>
      </div>

      <div id='Name'> 
        <h3> Name : </h3> <p> {userId} </p>
      </div>

      <div id='Personnality'> 
        <h3> Personnality </h3>
        <p> automatic / manuel </p>
      </div>

      <div id='launch'> 
        <h3> Launch Me ! </h3>
      </div>
      </div>

      
    </div>
      )
  }