import Navbar from "./Navbar"
import Popup from "./popupfeatures/popup"
import News from "./pages/News"
import Home from "./pages/Home"
import Performance from "./pages/Performance"
import Wallet from "./pages/Wallet"
import Aboutyou from "./pages/Aboutyou"
import Aboutus from "./pages/Aboutus"
import { Route, Routes } from "react-router-dom"




function App() {
  // Fonction qui recharge la page
  const reloadPage = () => {
    window.location.reload();
  };

  // Recharge la page toutes les 5 minutes
  setInterval(reloadPage, 5 * 60 * 1000);

  return (
    <>
      <div className="popup"> 
        <Popup/>
      </div>
      <Navbar />
        
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/News" element={<News />} />
        <Route path="/Performance" element={<Performance />} />
        <Route path="/Wallet" element={<Wallet />} />
        <Route path="/Aboutus" element={<Aboutus />} />
        <Route path="/Aboutyou" element={<Aboutyou />} />
      </Routes>
    </>
  )
}



export default App