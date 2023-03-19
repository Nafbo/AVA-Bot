import React, { useState } from 'react';
import { Link, useMatch, useResolvedPath } from "react-router-dom"
import img from './assets/avalogo.png'

export default function Navbar() {

  const [showMenu, setShowMenu] = useState(false);

  function handleMenuClick() {
    setShowMenu(!showMenu);
  }

  return (
    <nav className="nav">
      <div class="logo-container">
        <Link to="/" >
          <img src={require("./assets/avalogo.png")}  alt="menu icon"/>
        </Link>
      </div>
      
      <button class="menu-btn">
        <span class="menu-icon"></span>
      </button>

      <ul className='nav-links'>
       <li><CustomLink to="/">Home</CustomLink></li>
       <li><CustomLink to="/Performance">Performances</CustomLink></li>
       <li><CustomLink to="/News">News</CustomLink></li>
       <li><CustomLink to="/Wallet">Wallet</CustomLink></li>
       <li><CustomLink to="/aboutus">About Us</CustomLink></li>
      </ul>
      <Link to="/Aboutyou" className="logo">
         <img src={require("./assets/account.png")} alt="account icon"/>
      </Link>

    </nav>
  )
}  

function CustomLink({ to, children, ...props }) {
  const resolvedPath = useResolvedPath(to)
  const isActive = useMatch({ path: resolvedPath.pathname, end: true })

  return (
    <li className={isActive ? "active" : ""}>
      <Link to={to} {...props}>
        {children}
      </Link>
    </li>
  )
}