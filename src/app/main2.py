from fear_and_greed_analyse import check_fng_index
from influenceurs_analyse import analyse_sentiment_bitcoin
from fed_analyse import analyze_fed_news_for_btc
from whales_alert import analyze_whale_alert_tweets
from bitcoin_trend import average_trend
import time

def get_market_sentiment():


    fng = check_fng_index()
    
    #dxy = dxy_analyse.check_dxy_index()
    sentiment = analyse_sentiment_bitcoin()
    
    fed = analyze_fed_news_for_btc()
    
    whales = analyze_whale_alert_tweets()
    
    google_trend = average_trend()
    


    if fng == "vert" or fng == "neutre" and sentiment == 'confiant' and google_trend=='vogue' :
        print( "\nLe sentiment du marché est vert.\n")
    elif fng == "neutre" and sentiment == 'prudent' and google_trend=='vogue' :
        print("Le sentiment du marché est orange.\n")
    elif fng == "rouge" and sentiment == 'prudent'and google_trend=='pas_vogue' :
        print("Le sentiment du marché est rouge.\n")
    else:
        print("Le sentiment du marché est indéterminé.\n")
        
    print(fed+ "\n")
    
    print(whales)

get_market_sentiment()






