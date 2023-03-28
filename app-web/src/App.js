import Navbar from "./Navbar"
import Popup from "./popupfeatures/popup"
import News from "./pages/News"
import Home from "./pages/Home"
import Performance from "./pages/Performance"
import Wallet from "./pages/Wallet"
import Aboutyou from "./pages/Aboutyou"
import Aboutus from "./pages/Aboutus"
import { Route, Routes } from "react-router-dom"


import ChatBot, { Loading } from 'react-simple-chatbot';


const chatBot = {
  botName: "CryptoBot",
  backgroundColor: "#0080ff",
  avatarStyle: {
    borderRadius: "50%",
    backgroundColor: "#ffffff"
  },
  floating: true,
  floatingStyle: {
    right: "20px",
    bottom: "20px",
    backgroundColor: "#0080ff",
    color: "#ffffff"
  },
  steps: [
    {
      id: "1",
      message: "Bonjour, comment vous appelez-vous ?",
      trigger: "name"
    },
    {
      id: "name",
      user: true,
      trigger: "3"
    },
    {
      id: "3",
      message: "En quoi puis-je vous aider ?",
      trigger: "4"
    },
    {
      id: "4",
      options: [
        { value: "bitcoin", label: "Qu'est-ce que le Bitcoin ?", trigger: "5" },
        { value: "cryptocurrency", label: "Qu'est-ce qu'une cryptomonnaie ?", trigger: "6" }
      ]
    },
    {
      id: "5",
      message: "Le Bitcoin est une cryptomonnaie qui permet de réaliser des transactions de manière décentralisée et sécurisée. Sa particularité est qu'il n'est contrôlé par aucune autorité centrale, ce qui lui confère une grande indépendance.",
      trigger: "7"
    },
    {
      id: "6",
      message: "Une cryptomonnaie est une monnaie virtuelle utilisée pour effectuer des transactions. Elle est cryptée et décentralisée, ce qui signifie qu'elle n'est contrôlée par aucune autorité centrale. Les transactions sont validées grâce à un réseau de pairs qui vérifient les transactions les unes après les autres.",
      trigger: "7"
    },
    {
      id: "7",
      message: "Voulez-vous savoir autre chose ?",
      trigger: "8"
    },
    {
      id: "8",
      options: [
        { value: "yes", label: "Oui", trigger: "4" },
        { value: "no", label: "Non, merci", end: true }
      ]
    },
    {
      id: "end",
      message: "Au revoir !",
      end: true
    }
  ],
  delay: 1000 // Pause d'une seconde entre chaque message
};

      

function App() {
  // Fonction qui recharge la page
  const reloadPage = () => {
    window.location.reload();
  };

  // Recharge la page toutes les 5 minutes
  setInterval(reloadPage, 5 * 60 * 1000);

  return (
    <>
      <ChatBot {...chatBot} />
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