import "./perfo.css"
import Table from 'react-bootstrap/Table';
import Balanceft from "./features/perfofeatures"
import React, {Component} from "react"






class Performance extends Component{

  /* ------- API ------- */
  constructor(props) {
    super(props);
    this.state = {
      donnees: []
    };
  }

    componentDidMount(){
      fetch("https://ttwjs0n6o1.execute-api.eu-west-1.amazonaws.com/items/1",  )
        .then((response) => {
        return response.json()
        })
        .then((result) => {
          this.setState({donnees: result})
        })

        
    }
  
  /* ----------------------------------------------------------------------------- */
    
    render(){

      /* ---- Somme Balance ---- */
      let somme = 0;
      this.state.donnees.forEach(d => {
        somme += d.usd;
      });
      /* ---------------------- */

      

      return (

        <div className="perfo"> 
          
        
          <div id="balance"> 
            <h1> Balance </h1>
              <p  /* key={somme.id} */>{somme.toFixed(2)} USD</p>
          </div>


          <div id="currencies"> 
            <h1> CryptoCurrencies </h1>
            <table id="tableau">
              <thead>
                <tr>
                  <th>Symbol</th>
                  <th>Coins</th>
                </tr>
              </thead>
              <tbody>
                {this.state.donnees.map((d, i) => (
                  <tr key={i}>
                    <td>{d.symbol.substring(0, 3)}</td>
                    <td>{d.coins.toFixed(5)}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>

          
  
          <div id="running"> 
            <h1> Running </h1>
            <p> for 16 hours </p>
          </div>
  
          <div id="place"> 
            <h1> Place </h1>
            <p> binance </p>
          </div>
      
        
          <div id="transaction"> 
            <h1> Transactions </h1>
            <Table id="tabletransaction" striped bordered hover>
              <thead>
                <tr>
                  <th>From</th>
                  <th>To</th>
                  <th>Amount</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>49846543</td>
                  <td>519813</td>
                  <td>0.00005 E</td>
                </tr>
                <tr>
                  <td>54761876165416</td>
                  <td>61846747</td>
                  <td>0.56 C</td>
                </tr>
                <tr>
                  <td>8716</td>
                  <td>687419</td>
                  <td>0.5 Dash</td>
                </tr>
                <tr>
                  <td>54761876165416</td>
                  <td>61846747</td>
                  <td>0.56 C</td>
                </tr>
                <tr>
                  <td>54761876165416</td>
                  <td>61846747</td>
                  <td>0.56 C</td>
                </tr>
              </tbody>
            </Table> 
          </div>
        </div>
    )
  }
}

export default Performance