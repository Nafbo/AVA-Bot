from fear_and_greed_analyse import check_fng_index
from influenceurs_analyse import analyse_sentiment_bitcoin
from fed_analyse import analyze_fed_news_for_btc
from whales_alert import analyze_whale_alert_tweets
from bitcoin_trend import average_trend
import time

def get_market_sentiment():


    fng = check_fng_index()
    
    sentiment = analyse_sentiment_bitcoin()
    
    fed = analyze_fed_news_for_btc()
    
    whales = analyze_whale_alert_tweets()
    
    google_trend = average_trend()
    
    
    print("\nAnalyse du sentiment du marché concernant le Bitcoin :\n\nNoté de 1 à 5, 5 représentant le meilleur sentiment du marché.\n")


    if fng == "vert" or fng == "neutre" and sentiment == 'confiant' and google_trend=='vogue' and fed=="bonnes_nouvelles" or fed=="pas_de_nouvelles" and whales=="normal":
        print( "\n 5/5 \n")
    elif fng == "vert" or fng == "neutre" and sentiment == 'confiant' and google_trend=='vogue' and fed=="bonnes_nouvelles" or fed=="pas_de_nouvelles" and whales=="normal":
        print( "\n 5/5 \n")
    elif fng == "neutre" and sentiment == 'confiant' and google_trend=='vogue' or google_trend=='pas_vogue' and fed=="bonnes_nouvelles" or fed=="pas_de_nouvelles" and whales=="normal":
        print("\n 4/5 \n")
    elif fng == "neutre" and sentiment == 'confiant' and google_trend=='vogue' or google_trend=='pas_vogue' and fed=="bonnes_nouvelles" or fed=="pas_de_nouvelles" and whales=="normal":
        print("\n 4/5 \n")
    elif fng == "neutre" and sentiment == 'confiant' and google_trend=='pas_vogue' and fed=="bonnes_nouvelles" or fed=="pas_de_nouvelles" and whales=="normal":
        print("\n 3/5 \n")
    elif fng == "neutre" and sentiment == 'confiant' and google_trend=='pas_vogue' and fed=="bonnes_nouvelles" or fed=="pas_de_nouvelles" and whales=="normal":
        print("\n 3/5 \n")
    elif fng == "neutre" and sentiment == 'prudent' and google_trend=='pas_vogue' and fed=="mauvaises_nouvelles" and whales=="très_dangereux":
        print("\n 2/5 \n")
    elif fng == "neutre" and sentiment == 'prudent' and google_trend=='pas_vogue' and fed=="mauvaises_nouvelles" and whales=="dangereux":
        print("\n 2/5 \n")
    elif fng == "neutre" and sentiment == 'prudent' and google_trend=='pas_vogue' and fed=="pas_de_nouvelles" and whales=="très_dangereux":
        print("\n 2/5 \n")
    elif fng == "neutre" and sentiment == 'prudent' and google_trend=='pas_vogue' and fed=="pas_de_nouvelles" and whales=="dangereux":
        print("\n 2/5 \n")
    elif fng == "neutre" and sentiment == 'prudent' and google_trend=='pas_vogue' and fed=="mauvaises_nouvelles" or fed=="pas_de_nouvelles" and whales=="très_dangereux" or whales=="dangereux":
        print("\n 2/5 \n")
    elif fng == "rouge" and sentiment == 'prudent' and google_trend=='pas_vogue' and fed=="mauvaises_nouvelles" and whales=="très_dangereux":
        print("\n 1/5 \n")
    elif fng == "rouge" and sentiment == 'prudent' and google_trend=='pas_vogue' and fed=="mauvaises_nouvelles" and whales=="dangereux":
        print("\n 1/5 \n")
    elif fng == "rouge" and sentiment == 'prudent' and google_trend=='pas_vogue' and fed=="pas_de_nouvelles" and whales=="très_dangereux":
        print("\n 1/5 \n")
    elif fng == "rouge" and sentiment == 'prudent' and google_trend=='pas_vogue' and fed=="pas_de_nouvelles" and whales=="dangereux":
        print("\n 1/5 \n")
    elif fng == "rouge" and sentiment == 'prudent' and google_trend=='pas_vogue' and fed=="mauvaises_nouvelles" or fed=="pas_de_nouvelles" and whales=="très_dangereux" or whales=="dangereux":
        print("\n 1/5 \n")


        

get_market_sentiment()






