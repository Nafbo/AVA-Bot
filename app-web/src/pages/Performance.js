import "./styles/perfo.css"
import React, {Component} from "react"
import $ from 'jquery';
import 'datatables.net';






class Performance extends Component{

  /* ------- API ------- */
  constructor(props) {
    super(props);
    this.state = {
      donnees: []
    };
    this.tableRef = React.createRef();
  }
  
    componentDidMount(){
      fetch("https://ttwjs0n6o1.execute-api.eu-west-1.amazonaws.com/items/1",  )
        .then((response) => {
        return response.json()
        })
        .then((result) => {
          this.setState({donnees: result})
        }); 
        
      this.initDataTable();
        
    }


    initDataTable = () => {
      $(this.tableRef.current).DataTable({
        paging: true, // activer la pagination
        pageLength: 5, // par défaut, afficher 5 valeurs par page
        scrollY: '50%', // ajouter un scroll vertical à la table
        retrieve:true,
        lengthChange: true, // activer la modification de la longueur de page
        pageLengthOptions: [2, 4, 5] // définir les options de longueur de page
      });
    };


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
          
       {/* ----------------------------------------------------------------------------------------------------------------------------- */}

          <div id="balance"> 
            <h1> Balance </h1>
              <p  /* key={somme.id} */>{somme.toFixed(2)} USD</p>
          </div>

       {/* ----------------------------------------------------------------------------------------------------------------------------- */}

          <div id="currencies"> 
            <h1 id="title"> CryptoCurrencies </h1>
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
          
         {/* ----------------------------------------------------------------------------------------------------------------------------- */}

          <div id="running"> 
            <h1> Running </h1>
            <p> for 16 hours </p>
          </div>

         {/* ----------------------------------------------------------------------------------------------------------------------------- */}

          <div id="place"> 
            <h1> Place </h1>
            <p> binance </p>
          </div>

          {/* ----------------------------------------------------------------------------------------------------------------------------- */}
        
          <div id="transaction"> 
            <h1> Transactions </h1>
            <table id="tableau" ref={this.tableRef}>
              <thead>
                <tr>
                  <th>From</th>
                  <th>To</th>
                  <th>Amount</th>
                </tr>
              </thead>
              <tbody>
                {this.state.donnees.map((d, i) => (
                  <tr key={i}>
                    <td>{d.symbol.substring(0, 3)}</td>
                    <td>{d.coins.toFixed(5)}</td>
                    <td>{d.date}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>




          
        </div>
    )
  }
}

export default Performance