import getCookie from "./features/getcookies"
import image1 from '../assets/logo_simple.png';
import "./styles/aboutyou.css"

export default function Aboutyou() {
    const userId = getCookie('userId');

    document.addEventListener("DOMContentLoaded", function() {
        const logoutButton = document.getElementById("logoutaccount");

        logoutButton.addEventListener("click", () => {
            // Supprime les cookies de session
            document.cookie = "sessionKey=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
            document.cookie = "userId=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";

            alert(document.cookie);
            // Redirige vers la page de connexion ou d'accueil
            window.location.href = "connexion.html";
        });
    });

    return (
        <div className="account">
            
            <img id="logoava" src={image1}  alt="ava logo"/>     
            
            <div className="rightaccount">
                <h1 id="titleaccount">Welcome to your account</h1>
                <div id='idaccount'>
                    <h3>Your id</h3>
                    <h5>{userId}</h5>
                </div>
                <div id="passwordaccount">
                    <h3>Your password</h3>
                    <h5>password</h5>
                </div>
                <div id="apiaccount">
                    <h3>Your API</h3>
                    <h5 className="apiinfo">API Secret</h5>
                    <h5 className="apiinfo">API Key</h5>
                    <h5 className="apiinfo">API Password</h5>
                </div>
                <div id="telegramaccount">
                    <h3>Connect to Telegram?</h3>
                    <h5>chat id</h5> 
                </div>
            
                <button id="logoutaccount">Log out</button>
                
            </div>
        </div>
    )
}
