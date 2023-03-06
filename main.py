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
    fng = check_fng_index()
    sentiment = analyse_sentiment_bitcoin()
    fed = analyze_fed_news_for_btc()
    whales = analyze_whale_alert_tweets()
    google_trend = average_trend()
    
    print("\nAnalyse du sentiment du marché concernant le Bitcoin :\n\nNoté de 1 à 5, 5 représentant le meilleur sentiment du marché.\n")

    if fng == "vert" and sentiment == 'confiant' and google_trend=='vogue' and (fed=="bonnes_nouvelles" or fed=="pas_de_nouvelles") and whales=="normal":
        return "5/5"
    elif fng == "vert" and sentiment == 'confiant' and google_trend=='vogue' and (fed=="bonnes_nouvelles" or fed=="pas_de_nouvelles") and whales=="normal":
        return "5/5"
    elif fng == "vert" and sentiment == 'confiant' and (google_trend=='vogue' or google_trend=='pas_vogue') and (fed=="bonnes_nouvelles" or fed=="pas_de_nouvelles") and whales=="normal":
        return "4/5"
    elif (fng == "vert" or fng == "neutre") and sentiment == 'confiant' and (google_trend=='vogue' or google_trend=='pas_vogue') and (fed=="bonnes_nouvelles" or fed=="pas_de_nouvelles") and whales=="normal":
        return "3/5"
    elif fng == "neutre" and sentiment == 'confiant' and google_trend=='pas_vogue' and (fed=="bonnes_nouvelles" or fed=="pas_de_nouvelles") and whales=="normal":
        return "3/5"
    elif fng == "neutre" and sentiment == 'confiant' and google_trend=='pas_vogue' and (fed=="bonnes_nouvelles" or fed=="pas_de_nouvelles") and whales=="normal":
        return "3/5"
    elif fng == "neutre" and sentiment == 'prudent' and google_trend=='pas_vogue' and fed=="mauvaises_nouvelles" and whales=="très_dangereux":
        return "2/5"
    elif fng == "neutre" and sentiment == 'prudent' and google_trend=='pas_vogue' and fed=="mauvaises_nouvelles" and whales=="dangereux":
        return "2/5"
    elif fng == "neutre" and sentiment == 'prudent' and google_trend=='pas_vogue' and fed=="pas_de_nouvelles" and whales=="très_dangereux":
        return "2/5"
    elif fng == "neutre" and sentiment == 'prudent' and google_trend=='pas_vogue' and fed=="pas_de_nouvelles" and whales=="dangereux":
        return "2/5"
    elif fng == "neutre" and sentiment == 'prudent' and google_trend=='pas_vogue' and (fed=="mauvaises_nouvelles" or fed=="pas_de_nouvelles") and (whales=="très_dangereux" or whales=="dangereux"):
        return "2/5"
    elif fng == "rouge" and sentiment == 'prudent' and google_trend=='pas_vogue' and fed=="mauvaises_nouvelles" and whales=="très_dangereux":
        return "1/5"
    elif fng == "rouge" and sentiment == 'prudent' and google_trend=='pas_vogue' and fed=="mauvaises_nouvelles" and whales=="dangereux":
        return "1/5"
    elif fng == "rouge" and sentiment == 'prudent' and google_trend=='pas_vogue' and fed=="pas_de_nouvelles" and whales=="très_dangereux":
        return "1/5"
    elif fng == "rouge" and sentiment == 'prudent' and google_trend=='pas_vogue' and fed=="pas_de_nouvelles" and whales=="dangereux":
        return "1/5"
    elif fng == "rouge" and sentiment == 'prudent' and google_trend=='pas_vogue' and (fed=="mauvaises_nouvelles" or fed=="pas_de_nouvelles") and (whales=="très_dangereux" or whales=="dangereux"):
        return "1/5"
    

    
        

if __name__ == "__main__":
    sentiment_analyse = main()
    timestamp = str(int(time.time() * 1000))
    date = datetime.datetime.fromtimestamp(int(timestamp) / 1000.0)
    date_formatee = date.strftime('%Y-%m-%d %H:%M:%S')
    print(sentiment_analyse)
    myrow = {
        'user_name':date_formatee ,
        'sentiment_marche':sentiment_analyse
        }
    url ="https://u3ruvos9xf.execute-api.eu-west-1.amazonaws.com/items"
    rq.put(url, json=myrow, headers={'Content-Type': 'application/json'})
    