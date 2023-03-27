import React, { useEffect, useState, useMemo } from "react";
import Chart from 'chart.js/auto';
import getCookie from "./features/getcookies"



const SYMBOLS = ["BTC/USDT:USDT", "ETH/USDT:USDT", "DOGE/USDT:USDT", "LTC/USDT:USDT", "XRP/USDT:USDT"];



const id = getCookie('userId');
const API_ENDPOINT = `https://ttwjs0n6o1.execute-api.eu-west-1.amazonaws.com/items/${id}`;


const Wallet = () => {

  useEffect(() => {
    document.title = "AVABot Wallet"; 
  }, []);



  const [data, setData] = useState([]);

  const chartOptions = useMemo(() => ({
    scales: {
      xAxes: [
        {
          type: "time",
          time: {
            parser: "YYYY-MM-DD",
            tooltipFormat: "ll",
          },
          scaleLabel: {
            display: true,
            labelString: "Date",
          },
        },
      ],
      yAxes: [
        {
          scaleLabel: {
            display: true,
            labelString: "Wallet",
          },
        },
      ],
    },
  }), []);

  {//------------------------récupération des données avec l'API-------------------------//
  }

  useEffect(() => {
    const fetchData = async () => {
      const response = await fetch(API_ENDPOINT);
      const json = await response.json();
      setData(json.sort((a, b) => new Date(a.date) - new Date(b.date)));
    };

    fetchData();
  }, []);


  {//------------------------Premier graphique -------------------------//
  }

  useEffect(() => {
    if (data.length > 0) {
    

      const walletChartData = {
        labels: data.map((item) => item.date),
        datasets: [
          {
            label: "Wallet",
            data: data.map((item) => item.wallet),
            fill: false,
            borderColor: "rgba(75,192,192,1)",
          }
        ],
      };
    
      const walletChart = new Chart("walletChart", {
        type: "line",
        data: walletChartData,
        options: chartOptions,
      });
 

      return () => {
        walletChart.destroy();
      
      };
    }
  });

  {//------------------------graphique BTC -------------------------//
  }
  const [symbol, setSymbol] = useState(SYMBOLS[0]);

  useEffect(() => {
    if (data.length > 0) {
      const getchartData = (position, color) => {
        return data.filter((item) => item.position === position )
                   .map((item) => ({x: item.date, y: item.price, symbol: item.symbol}));
      };
      
      const btcPositionChartData = {
        labels: data.map((item) => item.date),
        datasets: [
          {
            label: "Open Long",
            data: getchartData("openLong", "green").filter((item) => item.symbol === symbol),
            fill: false,
            pointRadius: 6,
            pointHitRadius: 10,
          },
          {
            label: "Take Profit Hit",
            data: getchartData("takeProfitHit", "green").filter((item) => item.symbol === symbol),
            fill: false,
            pointRadius: 6,
            pointHitRadius: 10,
          },
          {
            label: "Open Short",
            data: getchartData("openShort", "red").filter((item) => item.symbol === symbol),
            fill: false,
            pointRadius: 6,
            pointHitRadius: 10,
          },
          {
            label: "Stop Loss Hit",
            data: getchartData("stopLossHit", "red").filter((item) => item.symbol === symbol),
            fill: false,
            pointRadius: 6,
            pointHitRadius: 10,
          },
        ],
    };

    const btcchartOptions = {
      scales: {
        xAxes: [
          {
            type: "time",
            time: {
              parser: "YYYY-MM-DD",
              tooltipFormat: "ll",
            },
            scaleLabel: {
              display: true,
              labelString: "Date",
            },
          },
        ],
        yAxes: [
          {
            scaleLabel: {
              display: true,
              labelString: "Price",
            },
          },
        ],
      },
    };

    const chart = new Chart("btcchart", {
      type: "line",
      data: btcPositionChartData,
      options: btcchartOptions,
    });
    return () => {
      chart.destroy();
    };
  }
}, [ data, symbol]);

  

  return (
    <div style={{padding : "2%"}}>
      <div> 
        <h1>Your Wallet </h1>
        <br />
        <br />
        <center>
        <h4>Total Wallet</h4></center>

      </div>
      <div>
        <canvas id="walletChart"></canvas>
      </div>

      <div>
        <br />

        <br />


        <br />
        <center>

        <h4>Buy&Sell</h4></center>
    
        </div>
        <div>
          <label htmlFor="symbol-select">Choose symbol :</label>
          <select id="symbol-select" value={symbol} onChange={(e) => setSymbol(e.target.value)}>
            {SYMBOLS.map((s) => (
              <option key={s} value={s}>
                {s}
              </option>
          ))}
        </select>
      </div>
        <canvas id="btcchart" width="800" height="400"></canvas>
      <br />
      <br />

      
    </div>
  );
};

export default Wallet;
    
    

