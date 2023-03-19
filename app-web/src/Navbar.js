import { Link, useMatch, useResolvedPath } from "react-router-dom"
import img from './assets/avalogo.png'

export default function Navbar() {
  return (
    <nav className="nav">
      <Link to="/" className="logo">
         <img src={require("./assets/avalogo.png")}/>
      </Link>

      <ul className="hpbh">
        <CustomLink to="/">Home</CustomLink>
        <CustomLink to="/Performance">Performance</CustomLink>
        <CustomLink to="/Backtests">Backtests</CustomLink>
        <CustomLink to="/History">History</CustomLink>
      </ul>

      <Link to="/Aboutyou" className="logo">
         <img src={require("./assets/account.png")}/>
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