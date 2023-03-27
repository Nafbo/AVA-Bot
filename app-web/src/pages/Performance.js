import "./styles/perfo.css"
import 'datatables.net';
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import getCookie from "./features/getcookies"



function Performance() {

  useEffect(() => {
    document.title = "AVABot Performances"; 
  }, []);


  useEffect(() => {
    const fetchData = async () => {
      // Récupération des dernières informations sur le Bitcoin
      const fetchCryptoData = async () => {
        const response = await fetch(
          'https://api.coingecko.com/api/v3/coins/bitcoin',
        );
        const data = await response.json();
        return {
          price: data.market_data.current_price.usd,
        };
      };}})
 
 
  const [data, setData] = useState([]);
  const [totalBalance, setTotalBalance] = useState(0);
  const [totalFees, setTotalFees] = useState(0);
  const [finalBalance, setFinalBalance] = useState(0);
  const [totalPerformances, setTotalPerformances] = useState(0);
  const [bestTrade, setBestTrade] = useState({});
  const [worstTrade, setWorstTrade] = useState({});
  const [pairStats, setPairStats] = useState([]);
  const [numOfTrades, setNumOfTrades] = useState(0);
  const [numOfPositives, setNumOfPositives] = useState(0);
  const [numOfNegatives, setNumOfNegatives] = useState(0);
  const [avgTradePerformance, setAvgTradePerformance] = useState(0);
  const [avgPositivePerformance, setAvgPositivePerformance] = useState(0);
  const [avgNegativePerformance, setAvgNegativePerformance] = useState(0);
  const [tradesWinRateRatio, setTradesWinRateRatio] = useState(0);
  const [numOfLongTrades, setNumOfLongTrades] = useState(0);
  const [AvgLongTradePerformance, setAvgLongTradePerformance] = useState(0);
  const [BestLongTrade, setBestLongTrade] = useState(0);
  const [WorstLongTrade, setWorstLongTrade] = useState(0);
  const [NumOfPositiveLongTrades, setNumOfPositiveLongTrades] = useState(0);
  const [NumOfNegativeLongTrades, setNumOfNegativeLongTrades] = useState(0);
  const [LongTradesWinRateRatio, setLongTradesWinRateRatio] = useState(0);
  const [numOfShortTrades, setNumOfShortTrades] = useState(0);
  const [AvgShortTradePerformance, setAvgShortTradePerformance] = useState(0);
  const [BestShortTrade, setBestShortTrade] = useState(0);
  const [WorstShortTrade, setWorstShortTrade] = useState(0);
  const [NumOfPositiveShortTrades, setNumOfPositiveShortTrades] = useState(0);
  const [NumOfNegativeShortTrades, setNumOfNegativeShortTrades] = useState(0);
  const [ShortTradesWinRateRatio, setShortTradesWinRateRatio] = useState(0);



  useEffect(() => {
    const id = getCookie('userId');
    const fetchData = async () => {
      const result = await axios(`https://ttwjs0n6o1.execute-api.eu-west-1.amazonaws.com/items/${id}`);
      setData(result.data);
    };
    fetchData();
  }, []);

  useEffect(() => {
    // calcul de la somme balance
    const balanceSum = data.reduce((acc, item) => acc + item.usd, 0);
    setTotalBalance(balanceSum);

    // calcul de la somme des frais
    const feesSum = data.reduce((acc, item) => acc + item.fees, 0);
    setTotalFees(feesSum);

    // récupération du solde final (dernière ligne de la colonne wallet)
    const finalWalletBalance = data[data.length - 1]?.wallet || 0;
    setFinalBalance(finalWalletBalance);

    // calcul de la somme des performances
    const performancesSum = data.reduce((acc, item) => {
      if (!isNaN(item.performance)) {
        return acc + item.performance;
      }
      return acc;
    }, 0);
    setTotalPerformances(performancesSum);

     // tri des données par date
     const sortedData = [...data].sort((a, b) => new Date(a.date) - new Date(b.date));


    // recherche de la meilleure performance
    const best = sortedData.reduce((max, item) => {
      if (!isNaN(item.performance) && item.performance > max.performance) {
        return item;
      }
      return max;
    }, { performance: -Infinity });
    setBestTrade(best);

    // recherche de la pire performance
    const worst = sortedData.reduce((min, item) => {
      if (!isNaN(item.performance) && item.performance < min.performance) {
        return item;
      }
      return min;
    }, { performance: Infinity });
    setWorstTrade(worst);

  // Calculating Pair Stats
  const pairs = [...new Set(data.filter((item) => !isNaN(item.performance)).map((item) => item.symbol))];
  const pairStats = pairs.map((pair) => {
    const filteredData = data.filter((item) => item.symbol === pair && !isNaN(item.performance));
    const trade = filteredData.length;
    const sumResult = filteredData.reduce((acc, item) => acc + item.performance, 0);
    const meanTrade = sumResult / filteredData.length;
    const worstTrade = Math.min(...filteredData.map((item) => item.performance));
    const bestTrade = Math.max(...filteredData.map((item) => item.performance));
    const goodTrades = filteredData.filter((item) => item.resultat === "good").length;
    const winRate = goodTrades / filteredData.length;
    return {
      trade,
      pair,
      sumResult,
      meanTrade,
      worstTrade,
      bestTrade,
      winRate,
    };
  });
  setPairStats(pairStats);

  // calculate trade info 

  const openPositions = data.filter((item) => item.position === "openLong" || item.position === "openShort");
  const numOfTrades = openPositions.length;
  const numOfPositives =data.filter((item) => item.resultat === "good").length;
  const numOfNegatives = data.filter((item) => item.resultat === "bad").length;
  // const sumAllPerformances = openPositions.reduce((acc, item) => {
  //   if (!isNaN(item.performance)) {
  //     return acc + parseFloat(item.performance);
  //   } else {
  //     return acc;
  //   }
  // }, 0);

  // const dfPosition = data.filter((row) => row.position === 'stopLossHit' || row.position === 'takeProfitHit' || row.position === 'closeShort' || row.position === 'closeLong');

  // let dfPositionLong = [];
  // let dfPositionShort = [];
  
  // for (let i = 0; i < dfPosition.length; i++) {
  //   const date = dfPosition[i].whenBuy;
  //   if (dfTrades[date].length !== 15) {
  //     for (let j = 0; j < dfTrades[date].length; j++) {
  //       if (dfTrades[date][j].position === 'openLong' && dfTrades[date][j].symbol === dfPosition[i].symbol) {
  //         dfPositionLong.push(dfPosition[i]);
  //       } else if (dfTrades[date][j].position === 'openShort' && dfTrades[date][j].symbol === dfPosition[i].symbol) {
  //         dfPositionShort.push(dfPosition[i]);
  //       }
  //     }
  //   } else {
  //     if (dfTrades[date].position === 'openLong' && dfTrades[date].symbol === dfPosition[i].symbol) {
  //       dfPositionLong.push(dfPosition[i]);
  //     } else if (dfTrades[date].position === 'openShort' && dfTrades[date].symbol === dfPosition[i].symbol) {
  //       dfPositionShort.push(dfPosition[i]);
  //     }
  //   }
  // }
  // dfPositionLong = dfPositionLong.map((row) => Object.values(row));
  // dfPositionShort = dfPositionShort.map((row) => Object.values(row));

  const sumPositivePerformances = openPositions.reduce((acc, item) => {
    if (item.resultat === "good" && !isNaN(item.performance)) {
      return acc + parseFloat(item.performance);
    } else {
      return acc;
    }
  }, 0);
  const sumNegativePerformances = openPositions.reduce((acc, item) => {
    if (item.resultat === "bad" && !isNaN(item.performance)) {
      return acc + parseFloat(item.performance);
    } else {
      return acc;
    }
  }, 0);
  const avgTradePerformance = performancesSum / numOfTrades;
  const avgPositivePerformance = sumPositivePerformances / numOfPositives;
  const avgNegativePerformance = sumNegativePerformances / numOfNegatives;
  const tradesWinRateRatio = numOfPositives / numOfTrades;

  setNumOfTrades(numOfTrades);
  setNumOfPositives(numOfPositives);
  setNumOfNegatives(numOfNegatives);
  setAvgTradePerformance(avgTradePerformance);
  setAvgPositivePerformance(avgPositivePerformance);
  setAvgNegativePerformance(avgNegativePerformance);
  setTradesWinRateRatio(tradesWinRateRatio);

  // Long trade info
let numOfLongTrades = 0;
let sumLongTradePerformance = 0;
let avgLongTradePerformance = 0;
let bestLongTrade = 0;
let worstLongTrade = 0;
let numOfPositiveLongTrades = 0;
let numOfNegativeLongTrades = 0;
let longTradesWinRateRatio = 0;

const filteredDatalong = data.filter((item) => item.position === "openLong" && !isNaN(item.performance));

if (filteredDatalong.length > 0) {
  numOfLongTrades = filteredDatalong.length;
  sumLongTradePerformance = filteredDatalong.reduce((acc, item) => acc + item.performance, 0);
  avgLongTradePerformance = sumLongTradePerformance / numOfLongTrades;
  bestLongTrade = filteredDatalong.reduce((prev, current) => (prev.performance > current.performance ? prev : current));
  worstLongTrade = filteredDatalong.reduce((prev, current) => (prev.performance < current.performance ? prev : current));
  numOfPositiveLongTrades = filteredDatalong.filter((item) => item.resultat === "good").length;
  numOfNegativeLongTrades = filteredDatalong.filter((item) => item.resultat === "bad").length;
  longTradesWinRateRatio = numOfPositiveLongTrades / numOfLongTrades;
}

  setNumOfLongTrades(numOfLongTrades);
  setAvgLongTradePerformance(avgLongTradePerformance);
  setBestLongTrade(bestLongTrade);
  setWorstLongTrade(worstLongTrade);
  setNumOfPositiveLongTrades(numOfPositiveLongTrades);
  setNumOfNegativeLongTrades(numOfNegativeLongTrades);
  setLongTradesWinRateRatio(longTradesWinRateRatio);

//short trade info
  // Number of Short trades
  
  let numOfShortTrades=0;
  let sumShortTradePerformance = 0;
  let avgShortTradePerformance = 0;
  let bestShortTrade = 0;
  let worstShortTrade = 0;
  let numOfPositiveShortTrades = 0;
  let numOfNegativeShortTrades = 0;
  let shortTradesWinRateRatio = 0;
  
  // Short trade info
  const filteredDatashort = data.filter((item) => item.position === "openShort" && !isNaN(item.performance));
  if (filteredDatalong.length > 0) {
  numOfShortTrades = filteredDatashort.length;
  sumShortTradePerformance = filteredDatashort.reduce((acc, item) => acc + item.performance, 0);
  avgShortTradePerformance = numOfShortTrades > 0 ? sumShortTradePerformance / numOfShortTrades : 0;
  bestShortTrade = filteredDatashort.reduce((prev, current) => (prev.performance > current.performance ? prev : current));
  worstShortTrade = filteredDatashort.reduce((prev, current) => (prev.performance < current.performance ? prev : current));
  numOfPositiveShortTrades = filteredDatashort.filter((item) => item.resultat === "good").length;
  numOfNegativeShortTrades = filteredDatashort.filter((item) => item.resultat === "bad").length;
  shortTradesWinRateRatio = numOfPositiveLongTrades / numOfLongTrades;
  }
  setNumOfShortTrades(numOfShortTrades);
  setAvgShortTradePerformance(avgShortTradePerformance);
  setBestShortTrade(bestShortTrade);
  setWorstShortTrade(worstShortTrade);
  setNumOfPositiveShortTrades(numOfPositiveShortTrades);
  setNumOfNegativeShortTrades(numOfNegativeShortTrades);
  setShortTradesWinRateRatio(shortTradesWinRateRatio);

  }, [data]);


      return (

      <div className="perfo"> 
          
       {/* ----------------------------------------------------------------------------------------------------------------------------- */}
          <div className="gauche"> 
          <div id="balance"> 
            <h1> Balance </h1>
              <p id="insidebalance">{finalBalance.toFixed(2)} USD</p>
          </div>

       {/* ----------------------------------------------------------------------------------------------------------------------------- */}

        <div id="generalinfo"> 
          <h1> General Informations </h1>
          <br/>
          <p> Total fees : {totalFees.toFixed(2)} $ </p>
          <p> Performances : {totalPerformances.toFixed(2)} % </p>
          <p> Performance du Bitcoin : {} $ </p>
          <p> Best trade : {parseFloat(bestTrade.performance).toFixed(2)} % ({bestTrade.date})</p>
          <p> Worst trade : {parseFloat(worstTrade.performance).toFixed(2)} % ({worstTrade.date}) </p>
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
            {pairStats.map((pairStat, index) => (
              <tr key={index}>
                <td>{pairStat.trade}</td>
                <td>{pairStat.pair.slice(0, 3)}</td>
                <td>{parseFloat(pairStat.sumResult).toFixed(2)} %</td>
                <td>{parseFloat(pairStat.meanTrade).toFixed(2)} %</td>
                <td>{parseFloat(pairStat.worstTrade).toFixed(2)} %</td>
                <td>{parseFloat(pairStat.bestTrade).toFixed(2)} %</td>
                <td>{(pairStat.winRate * 100).toFixed(2)} %</td>
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
                <h1> Trades Informations </h1>
                <h5> (Positions openLong & openShort) </h5>
                <br/>
                <p>Number of trades: {numOfTrades}</p>
                <p>Number of positive trades: {numOfPositives}</p>
                <p>Number of negative trades: {numOfNegatives}</p>
                <p>Trades win rate ratio: {tradesWinRateRatio.toFixed(2)}</p>
                <p>Average trades performances: {avgTradePerformance.toFixed(2)}</p>
                <p>Average positive performances: {avgPositivePerformance.toFixed(2)}</p>
                <p>Average negative performances: {avgNegativePerformance.toFixed(2)}</p>
              </div>

              <div id="longtradeinfo"> 
                <h1> Long Trades Information </h1>
                <h5> (Positions openLong) </h5>
                <p> Number of long trades: {numOfLongTrades} </p>
                <p> Average long trades performances: {AvgLongTradePerformance}  </p>
                <p> Best long trade: {BestLongTrade}</p>
                <p> Worst long trade : {WorstLongTrade} </p>
                <p> Number of positives long trades: {NumOfPositiveLongTrades}  </p>
                <p> Number of negatives long trades : {NumOfNegativeLongTrades} </p>
                <p> Long trade win rate ratio : {LongTradesWinRateRatio} </p>
              </div>

              <div id="shorttradeinfo"> 
                <h1> Short Trades Information</h1>
                <h5> (Positions openShort) </h5>
                <p> Number of short trades: {numOfShortTrades} </p>
                <p> Average short trades performances: {AvgShortTradePerformance}  </p>
                <p> Best short trade: {BestShortTrade} </p>
                <p> Worst short trade: {WorstShortTrade}  </p>
                <p> Number of positives short trades: {NumOfPositiveShortTrades}  </p>
                <p> Number of negatives long trades: {NumOfNegativeShortTrades}  </p>
                <p> Long trade win rate ratio: {ShortTradesWinRateRatio}  </p>
              </div>
          </div>



          
        </div>
    )
  }

export default Performance