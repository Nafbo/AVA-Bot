import Navbar from "./Navbar"
import Backtests from "./pages/Backtests"
import Home from "./pages/Home"
import Performance from "./pages/Performance"
import History from "./pages/History"
import { Route, Routes } from "react-router-dom"

import Particles from "react-tsparticles";
import { loadFull } from "tsparticles";

function App() {
  return (
    <>
      <Navbar />
      <div className="container">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/Backtests" element={<Backtests />} />
          <Route path="/Performance" element={<Performance />} />
          <Route path="/History" element={<History />} />
        </Routes>
      </div>
      
    </>
  )
}

export default App