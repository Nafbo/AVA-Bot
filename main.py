import warnings
import time
import datetime
import requests as rq
warnings.filterwarnings('ignore')
from src.app.fear_and_greed_analyse import check_fng_index
from src.app.influenceurs_analyse import analyse_sentiment_bitcoin
from src.app.fed_analyse import analyze_fed_news_for_btc
from src.app.whales_alert import analyze_whale_alert_tweets
from src.app.bitcoin_trend import average_trend

def main():
    analysis = Analysis()
    pairList = ['BTC/USDT', 'ETH/USDT', 'BNB/USDT', 'XRP/USDT', 'ADA/USDT']
    return(analysis.analyzeBacktest(pairList, '1h',usd = 100, start_date='2022-01-01'))

if __name__ == '__main__':
    print(main())