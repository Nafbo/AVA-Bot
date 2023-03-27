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



  constructor(props) {
    super(props);
    this.state = {
      donnees: [],
      maxpos: '',
      pairlist: [],
      isLaunched: false,
      running: false,
    };
    this.tableRef = React.createRef();
    this.handleSubmit = this.handleSubmit.bind(this)

    
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
        body: JSON.stringify({ maxActivePositions: this.state.maxpos}),
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
    
    handleCheckboxChange = (event) => {
      const isChecked = event.target.checked;
      const value = event.target.value;
      const pairlist = [...this.state.pairlist];
    
      if (isChecked) {
        pairlist.push(value);
      } else {
        const index = pairlist.indexOf(value);
        if (index !== -1) {
          pairlist.splice(index, 1);
        }
      }
    
      this.setState({ pairlist });
  };

  handleSubmit = (e) => {

      e.preventDefault();
      const id = getCookie('userId');
      console.log("clique")
      const { maxpos, pairlist } = this.state;
    
      const pairlist2 = pairlist
      .filter((value) => value)
      .map((value) => value);

      console.log(pairlist2);
        

      fetch(`https://wklab094d7.execute-api.eu-west-1.amazonaws.com/items/${id}`, {
        method: 'PATCH',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ 	
          maxActivePositions: maxpos,
           pairList: pairlist2 })
      })
      .then(response => response.json())
      .then(data => {
        console.log('Data updated:', data);
        // Update the component state with the updated data if necessary
      })
      .catch(error => {
        console.error('Error updating data:', error);
      });
    }
  

    handleClick = () => {
      const id = getCookie('userId');
      const { isLaunched}= this.state;
      const running = !isLaunched;
      const currentDate = new Date().toISOString();

      console.log(currentDate);
  
      axios.patch(`https://wklab094d7.execute-api.eu-west-1.amazonaws.com/items/${id}`, { running, startingDate: currentDate})
        .then(response => {
          this.setState({
            isLaunched: !isLaunched,
            running: running,
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
                    <label htmlFor="pairlist">Choose your pairlist</label>
                    
                      <div className='principale'> 
                      <div className='ligne1'> 
                        <input type="checkbox" id="BTC" name="pairlist" value="BTC/USDT:USDT" onChange={this.handleCheckboxChange} />
                        <label htmlFor="BTC">BTC/USDT:USDT</label>
                        
                        <input type="checkbox" id="ETH" name="pairlist" value="ETH/USDT:USDT" onChange={this.handleCheckboxChange} />
                        <label htmlFor="ETH">ETH/USDT:USDT</label>
                        
                        <input type="checkbox" id="XRP" name="pairlist" value="XRP/USDT:USDT" onChange={this.handleCheckboxChange} />
                        <label htmlFor="XRP">XRP/USDT:USDT</label>
                        
                        <input type="checkbox" id="EOS" name="pairlist" value="EOS/USDT:USDT" onChange={this.handleCheckboxChange} />
                        <label htmlFor="EOS">EOS/USDT:USDT</label>
                        
                        <input type="checkbox" id="BCH" name="pairlist" value="BCH/USDT:USDT" onChange={this.handleCheckboxChange} />
                        <label htmlFor="BCH">BCH/USDT:USDT</label>

                        </div>
                        <div className='ligne2'>
                        
                        <input type="checkbox" id="LTC" name="pairlist" value="LTC/USDT:USDT" onChange={this.handleCheckboxChange} />
                        <label htmlFor="LTC">LTC/USDT:USDT</label>
                       
                        <input type="checkbox" id="ADA" name="pairlist" value="ADA/USDT:USDT" onChange={this.handleCheckboxChange} />
                        <label htmlFor="ADA">ADA/USDT:USDT</label>
                        
                        <input type="checkbox" id="ETC" name="pairlist" value="ETC/USDT:USDT" onChange={this.handleCheckboxChange} />
                        <label htmlFor="ETC">ETC/USDT:USDT</label>
                        
                        <input type="checkbox" id="LINK" name="pairlist" value="LINK/USDT:USDT" onChange={this.handleCheckboxChange} />
                        <label htmlFor="EOS">LINK/USDT:USDT</label>
                       
                        <input type="checkbox" id="TRX" name="pairlist" value="TRX/USDT:USDT" onChange={this.handleCheckboxChange} />
                        <label htmlFor="TRX">TRX/USDT:USDT</label>

                        </div>
                        <div className='ligne3'>
                        
                        <input type="checkbox" id="DOT" name="pairlist" value="DOT/USDT:USDT" onChange={this.handleCheckboxChange} />
                        <label htmlFor="DOT">DOT/USDT:USDT</label>
                        
                        <input type="checkbox" id="DODGE" name="pairlist" value="DODGE/USDT:USDT" onChange={this.handleCheckboxChange} />
                        <label htmlFor="DODGE">DODGE/USDT:USDT</label>

                        <input type="checkbox" id="SOL" name="pairlist" value="SOL/USDT:USDT" onChange={this.handleCheckboxChange} />
                        <label htmlFor="SOL">SOL/USDT:USDT</label>
                        
                        <input type="checkbox" id="MATIC" name="pairlist" value="MATIC/USDT:USDT" onChange={this.handleCheckboxChange} />
                        <label htmlFor="MATIC">MATIC/USDT:USDT</label>
                        
                        <input type="checkbox" id="BNB" name="pairlist" value="BNB/USDT:USDT" onChange={this.handleCheckboxChange} />
                        <label htmlFor="BNB">BNB/USDT:USDT</label>

                        </div>
                        <div className='ligne4'>

                        <input type="checkbox" id="UNIU" name="pairlist" value="UNIU/USDT:USDT" onChange={this.handleCheckboxChange} />
                        <label htmlFor="UNIU">UNIU/USDT:USDT</label>

                        <input type="checkbox" id="THETA" name="pairlist" value="THETA/USDT:USDT" onChange={this.handleCheckboxChange} />
                        <label htmlFor="THETA">THETA/USDT:USDT</label>

                        <input type="checkbox" id="AVAX" name="pairlist" value="AVAX/USDT:USDT" onChange={this.handleCheckboxChange} />
                        <label htmlFor="AVAX">AVAX/USDT:USDT</label>

                        <input type="checkbox" id="SHIBU" name="pairlist" value="SHIBU/USDT:USDT" onChange={this.handleCheckboxChange} />
                        <label htmlFor="SHIBU">SHIBU/USDT:USDT</label>

                        <input type="checkbox" id="MANA" name="pairlist" value="MANA/USDT:USDT" onChange={this.handleCheckboxChange} />
                        <label htmlFor="MANA">MANA/USDT:USDT</label>

                        </div>
                        <div className='lignedubas'>
                        

                        <input type="checkbox" id="GALA" name="pairlist" value="GALA/USDT:USDT" onChange={this.handleCheckboxChange} />
                        <label htmlFor="GALA">GALA/USDT:USDT</label>

                        <input type="checkbox" id="SAND" name="pairlist" value="SAND/USDT:USDT" onChange={this.handleCheckboxChange} />
                        <label htmlFor="SAND">SAND/USDT:USDT</label>

                        </div>

                        </div>
                        
                    <p> actual pairlist : {/* {this.state.donnees[0]?.pairList} */}</p>  
                  </form> 
                  <button type="submit" onClick={this.handleSubmit}>Save these preferences</button>
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