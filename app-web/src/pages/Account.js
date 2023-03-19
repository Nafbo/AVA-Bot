import getCookie from "./features/getcookies"
import image1 from '../assets/robot1.png';
import "./styles/account.css"

export default function Account() {
    const userId = getCookie('userId');

    const logoutButton = document.getElementById("logoutaccount");

    logoutButton.addEventListener("click", () => {
    // Supprime le cookie de session
    document.cookie = "sessionkey=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
    // Redirige vers la page de connexion ou d'accueil
    window.location.href = "connexion.html";
    });

    return (
        <div className="account"> 

            <div className="leftaccount"> 
                <img id="imagerobot" src={image1}  alt="robot 1"/>     
            </div>

            <div className="rightaccount"> 
                <h1 id="titleaccount">Welcome to your account </h1>

                <div id='idaccount'> 
                    <h3> Your id </h3> 
                    <h5> {userId}</h5>
                </div>

                <div id="passwordaccount">
                    <h3> Your password </h3> 
                    <h5> password  </h5>
                </div>

                <div id="apiaccount">
                    <h3> Your API</h3>   
                    <h5 className="apiinfo"> API Secret  </h5>
                    <h5 className="apiinfo"> API Key  </h5>
                    <h5 className="apiinfo"> API Password  </h5>
                </div>

                <div id="telegramaccount">
                    <h3> Connect to telegam ?</h3>  
                    <h5> chat id  </h5> 
                </div>

                <div id="logoutaccount">
                    <h5> Log out</h5>   
                </div>

            </div>
        </div>
    )
  }