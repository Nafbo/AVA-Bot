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
          <div className="gauche"> 
          <div id="balance"> 
            <h1> Balance </h1>
              <p  /* key={somme.id} */>{somme.toFixed(2)} USD</p>
          </div>

       {/* ----------------------------------------------------------------------------------------------------------------------------- */}

        <div id="generalinfo"> 
          <h1> General Informations </h1>
          <p> Total fees </p>
          <p> Final Balance </p>
          <p> Performances </p>
          <p> Buy&Hold </p>
          <p> Performance vs Buy&Hold </p>
          <p> Best trade </p>
          <p> Worst trade </p>
        </div>

        {/* ----------------------------------------------------------------------------------------------------------------------------- */}


       {/* ----------------------------------------------------------------------------------------------------------------------------- */}

          <div id="currencies"> 
            <h1> Pair Result</h1>
            <table id="tableau">
                  <thead>
                    <tr>
                      <th>Trades</th>
                      <th>Pair</th>
                      <th>Sum-result</th>
                      <th>Mean-Trade</th>
                      <th>Worst-Trade</th>
                      <th>Best-Trade</th>
                      <th>Win-Rate</th>
                    </tr>
                  </thead>
                  <tbody>
                    {this.state.donnees.map((d, i) => (
                      <tr key={i}>
                        <td>{d.symbol.substring(0, 3)}</td>
                        <td>{d.coins.toFixed(5)}</td>
                        <td>{d.coins.toFixed(5)}</td>
                        <td>{d.coins.toFixed(5)}</td>
                        <td>{d.coins.toFixed(5)}</td>
                        <td>{d.coins.toFixed(5)}</td>
                        <td>{d.coins.toFixed(5)}</td>
                      </tr>
                    ))}
                  </tbody>
                </table> 
          </div>
          

          <div id="place"> 
            <h1> Running Information</h1>
            <p> Bot on  </p>
            <p> Starting date  </p>
            <p> Ending date  </p>
            <p> Starting balance  </p>
            <p> Leverage use  </p>
          </div>

          {/* ----------------------------------------------------------------------------------------------------------------------------- */}
          </div>

          <div id="droite"> 
              <div id="tradeinfo"> 
                <h1> Trades Informations</h1>
                <p> Number of trades </p>
                <p> Number of positives trades  </p>
                <p> Number of negatives trades  </p>
                <p> Trades win rate ratio  </p>
                <p> Average trades performances  </p>
                <p> Average positive performances  </p>
                <p> Average negative performances  </p>
              </div>

              <div id="longtradeinfo"> 
                <h1> Long Trades Information</h1>
                <p> Number of long trades </p>
                <p> Average long trades performances  </p>
                <p> Best long trade </p>
                <p> Worst long trade  </p>
                <p> Number of positives long trades  </p>
                <p> Number of negatives long trades  </p>
                <p> Long trade win rate ratio  </p>
              </div>

              <div id="shorttradeinfo"> 
                <h1> Short Trades Information</h1>
                <p> Number of short trades </p>
                <p> Average short trades performances  </p>
                <p> Best short trade </p>
                <p> Worst short trade  </p>
                <p> Number of positives short trades  </p>
                <p> Number of negatives long trades  </p>
                <p> Long trade win rate ratio  </p>
              </div>



            {/* <h1> Transactions </h1>
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
            </table> */}
          </div>



          
        </div>
    )
  }
}

export default Performance