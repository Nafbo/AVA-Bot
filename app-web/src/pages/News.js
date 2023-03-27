
import React, { useState, useEffect, useRef } from 'react';
import Chart from 'chart.js/auto';
import 'bootstrap/dist/css/bootstrap.min.css';
import { TwitterTimelineEmbed } from 'react-twitter-embed';


function News() {
 
  useEffect(() => {
    document.title = "AVABot News"; // Remplacez "Titre de MaPage" par le titre de votre choix pour cette page
  }, []);

  const [data, setData] = useState('');
  const chartRef = useRef('');
 

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
          market_cap: data.market_data.market_cap.usd,
          high_24h: data.market_data.high_24h.usd,
          low_24h: data.market_data.low_24h.usd
        };
      };

      // Récupération du Fear and Greed Index actuel
      const fetchFearAndGreedHistory = async () => {
        const response = await fetch(
          'https://api.alternative.me/fng/?limit=30',
        );
        const data = await response.json();
        return data.data.map(item => ({
          date: new Date(item.timestamp * 1000),
          value: item.value
        }));
      };

     

      // Appel des fonctions pour récupérer les données
      const cryptoData = await fetchCryptoData();
      const fearAndGreedHistory = await fetchFearAndGreedHistory();

      // Stocker les données dans l'état local
      setData({cryptoData, fearAndGreedHistory});
    };

    fetchData().catch(error => {
      console.error(error);
    });
  }, []);

  useEffect(() => {
    if (data) {
      if (chartRef.current.chart) {
        chartRef.current.chart.destroy();
      }
      // Créer le graphique
      const sortedData=data.fearAndGreedHistory.sort((a,b)=> a.date - b.date);
      const ctx = chartRef.current.getContext('2d');
      const chart = new Chart(ctx, {
        type: 'line',
        data: {
          labels: sortedData.map(item => item.date.toLocaleDateString()),
          datasets: [{
            label: 'Fear and Greed Index',
            data: sortedData.map(item => item.value),
            borderColor: 'rgba(255, 99, 132, 1)',
            backgroundColor: 'rgba(255, 99, 132, 0.2)',
            borderWidth: 1
          }]
        },
        options: {
          scales: {
            xAxes: [{
              type: 'time',
              time: {
                unit: 'day'
              }
            }],
            yAxes: [{
              ticks: {
                beginAtZero: true
              }
            }]
          }
        }
      });
      chartRef.current.chart = chart;
    }
  }, [data]);

  return (
    <div>
      <h1>News about cryptocurrencies</h1>
      {data && (
        <>  
          <br/>
          <br/>
          <table className="table table-striped">
            <thead> 
              <tr>
                <h5>News about the Bitcoin </h5>
                <br/>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Price (USD)</td>
                <td>{data.cryptoData.price} $</td>
              </tr>
              <tr>
                <td>Market capitalisation (USD)</td>
                <td>{data.cryptoData.market_cap} $</td>
              </tr>
              <tr>
                <td>Highest (24h) (USD)</td>
                <td>{data.cryptoData.high_24h} $</td>
              </tr>
              <tr>
                <td>Lowest (24h) (USD)</td>
                <td>{data.cryptoData.low_24h} $</td>
              </tr>
            </tbody>
          </table>

          <br/>
          <br/>

          <div>
            <tr>
              <h5>Fear and Greed Index (real-time) : </h5>
              <br/>
              <th></th>
            </tr>
            <canvas ref={chartRef}></canvas>
          </div>

          <br/>
          <br/>

          <div style={{ display: 'flex' }}>
            <div style={{ float: 'left', width: '50%' }}>
              <TwitterTimelineEmbed
                sourceType="list"
                ownerScreenName="AD87624"
                slug="1637559740443111430"
                options={{ height: 800, width: 550 }}
              />
            </div>
            <div style={{ float: 'left', width: '50%' }}>
              <TwitterTimelineEmbed
                sourceType="list"
                ownerScreenName="AD87624"
                slug="1637841452448329728"
                options={{ height: 800, width: 550 }}
              />
            </div>
          </div>


          
        </>
      )}
      
    </div>
  );
};

export default News;



