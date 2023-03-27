
/* import { Carousel } from 'react-bootstrap'; */
import image1 from '../assets/robot1.png';
/* import image2 from '../assets/robot2.png';
import image3 from '../assets/robot3.png';
import image4 from '../assets/robot4.png'; */
import 'bootstrap/dist/css/bootstrap.min.css';
import "./styles/home.css";
import getCookie from "./features/getcookies";/* om "react"; */
import React, {Component} from "react" ;
import axios from 'axios';;

class Home extends Component {

 
  /* const [APIkey, setApiKey] = useState(''); */


  constructor(props) {
    super(props);
    this.state = {
      donnees: [],
      maxpos: '',
      pairlist: '',
      isLaunched: false,
      running: false,
    };
    this.tableRef = React.createRef();

    
  }
  
    componentDidMount(){
      document.title = "AVABot";
      const id = getCookie('userId');
      fetch(`https://wklab094d7.execute-api.eu-west-1.amazonaws.com/items/${id}`,  )
        .then((response) => {
        return response.json()
        })
        .then((result) => {
          console.log(result)
          this.setState({ donnees: result })
        }); 
    }

    hideandshow = () => {
      var x = document.getElementById("divhide");
      const manualButton = document.querySelector(".manuel");
      if (x.style.display === "none") {
        x.style.display = "block";
        manualButton.classList.add("active");
      } else {
        x.style.display = "none";
        manualButton.classList.remove("active");
      }
    }

    handleOptionClick = (value) => {
          const id = getCookie('userId');
          const requestOptions = {
            method: 'PATCH',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ withMode: value })
          };
          fetch(`https://wklab094d7.execute-api.eu-west-1.amazonaws.com/items/${id}`, requestOptions)
            .then((response) => {
              if (!response.ok) {
                throw new Error('Failed to update personality.');
              }
            })
            .catch((error) => {
              console.log(error);
            }) 
        }
  
    handleAutomaticClick = () => {  
      const id = getCookie('userId');
     const divHideElement = document.getElementById("divhide");
      const requestOptions = {
        method: 'PATCH',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ mode: 'automatic' })
      };
      fetch(`https://wklab094d7.execute-api.eu-west-1.amazonaws.com/items/${id}`, requestOptions)
        .then((response) => {
          if (!response.ok) {
            throw new Error('Failed to update personality.');
          }
          divHideElement.style.display = "none";
        })
        .catch((error) => {
          console.log(error);
        });
    }

  
    handleManualClick = () => {
      const id = getCookie('userId');
      const requestOptions = {
        method: 'PATCH',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ mode: 'manual' })
      };
      fetch(`https://wklab094d7.execute-api.eu-west-1.amazonaws.com/items/${id}`, requestOptions)
        .then((response) => {
          if (!response.ok) {
            throw new Error('Failed to update personality.');
          }
          this.hideandshow();
        })
        .catch((error) => {
          console.log(error);
        }) 
    }

    updateData = () => {
      const id = getCookie('userId');
      const requestOptions = {
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ maxActivePositions: this.state.maxpos, pairlist: this.state.pairlist }),
      };
      fetch(`https://wklab094d7.execute-api.eu-west-1.amazonaws.com/items/${id}`, requestOptions )
        .then((response) => {
          if (!response.ok) {
            throw new Error("Failed to update data.");
          }
          console.log("Data updated successfully.");
        })
        .catch((error) => {
          console.log(error);
        });
    };

    handleSubmit = (event) => {
      event.preventDefault();
      this.updateData();
    };

    handleClick = () => {
      const id = getCookie('userId');
      const { isLaunched}= this.state;
      const running = !isLaunched;
  
      axios.patch(`https://wklab094d7.execute-api.eu-west-1.amazonaws.com/items/${id}`, { running })
        .then(response => {
          this.setState({
            isLaunched: !isLaunched,
            running: running
          });
        })
        .catch(error => {
          console.error(error);
        });
    }
    

    
    render(){
      const launchClass = this.state.isLaunched ? 'launch--stopped' : 'launch--launched';
      return(
    
        <div className='home'> 
          
          <div id="gauche">
            <img src={image1} id="robot1" alt="robot 1"/>     
          </div>

          <div className='droite'> 
            <div id='Title'>
              <h1> Your AVA Bot</h1>
            </div>

          
            <div className='gauche2'> 

              <div id='Name'> 
                <h3> Name  </h3> <p> {this.state.donnees[0]?.username} </p>
              </div>

              <div id='Personnality'> 
                <h3> Personality </h3>
                <p> <button className='auto' onClick={this.handleAutomaticClick}> automatic </button> <button  className={`manuel ${this.state.withMode === 'manual' ? 'active' : ''}`} onClick={this.handleManualClick} > manual </button>  </p>
                
                <div id="divhide" style = {{display:"none"}}>
                  <h5> - Manual mode activated - </h5>
                  <h3>Choose your bot's personality</h3>
                  <button className="calm" onClick={() => this.handleOptionClick('calm')} > calm </button> 
                  <button className="medium" onClick={() => this.handleOptionClick('medium')}> medium </button> 
                  <button className="aggressive" onClick={() => this.handleOptionClick('aggressive')}> aggressive </button>  
                </div>

              </div>

            </div>


            <div className="droite2"> 
                <div id='Options'> 
                  <h3> Options </h3>
                  <form onSubmit={this.handleSubmit}>
                    <label htmlFor="maxpos">Maximum Open Position</label>
                    <input value={this.state.maxpos} onChange={(e) => this.setState({maxpos: e.target.value})}  id="maxpos" placeholder="how many do you want?" required/>
                    <p> actual open position : {this.state.donnees[0]?.maxActivePositions}</p>
                    <br/>
                    <label htmlFor="pairlist">Pairlist</label>
                    <input value={this.state.pairlist} onChange={(e) => this.setState({pairlist: e.target.value})} id="pairlist" placeholder="Pairlist" required/>
                    <p> actual pairlist : {this.state.donnees[0]?.pairList}</p>  
                  </form> 
                  <button type="submit">Save these preferences</button>
                </div>
            </div>

          

        
          
            <button className={`launch ${launchClass}`}  onClick={this.handleClick}>
                {this.state.isLaunched ? 'Stop me ! ' : 'Launch me !'}
            </button>

          </div> 

          
        </div>
          )
    }
    
  }

  export default Home