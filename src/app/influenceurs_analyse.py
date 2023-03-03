import tweepy
import pandas as pd
from textblob import TextBlob
import warnings
warnings.filterwarnings("ignore")

def analyse_sentiment_bitcoin():
    '''Using the twitter API to retrieve the latest tweets from somes bitcoin influencers accounts about BTC, using Tweepy to know the polarity of tweets

    
        Returns:
        Return(String): confident or cautious if it's a good or bad news

    '''
    # Configuration de l'API Twitter
    consumer_key = "88dldRnuq6fLPQKkX8azrCd5p"
    consumer_secret = "WTZDb3JRQUjZVRu6LhQNhIVzoQpZ2Cd2i6ePKnRATeQnBuNx6g"
    access_token = "1435977329524752387-xa4DXdjkxgYNhbBJbdJZgySGC2YjRy"
    access_token_secret = "CneEP3iDzDhiho3UDhAFjnPTvdUBcVAsluoH574urkINb"

    # Connexion à l'API
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    # Recherche des tweets contenant le mot "Bitcoin"
    # Liste des influenceurs
    influencers = ['DocumentingBTC', 'MartyBent', 'lopp', 'nic__carter', 'Gladstein', 'BTC_Archive', 'natbrunell', '100trillionUSD', 'MessariCrypto', 'aantonop', 'VitalikButerin', 'SatoshiLite', 'NickSzabo4', 'rogerkver', 'aantonop', 'ErikVoorhees', 'brian_armstrong',' bgarlinghouse','cz_binance','bfmCrypto','crypto_futur','PowerHasheur','JulienROMAN13']

    # Initialisation d'un DataFrame vide
    df_tweets = pd.DataFrame(columns=['username', 'text', 'date'])

    # Récupération des tweets de chaque influenceur
    for influencer in influencers:
        tweets = api.user_timeline(screen_name=influencer, count=200)
        for tweet in tweets:
            df_tweets = df_tweets.append({'username': tweet.user.screen_name, 'text': tweet.text, 'date': tweet.created_at}, ignore_index=True)


    # Nettoyage des tweets (suppression des mentions, des liens, etc.)
    df_tweets['text'] = df_tweets['text'].str.replace('@\w+', '')
    df_tweets['text'] = df_tweets['text'].str.replace('http\S+', '')

    # Vérification du sentiment des tweets
    df_tweets['polarity'] = df_tweets['text'].apply(lambda x: TextBlob(x).sentiment.polarity)

    # Sélection des tweets ayant un sentiment positif ou négatif
    df_positive_tweets = df_tweets[df_tweets['polarity'] > 0]
    df_negative_tweets = df_tweets[df_tweets['polarity'] < 0]

    # Affichage des résultats
    #print("Il y a actuellement {} tweets positifs sur Bitcoin sur Twitter.".format(len(df_positive_tweets)))
    #print("Il y a actuellement {} tweets négatifs sur Bitcoin sur Twitter.".format(len(df_negative_tweets)))

    if len(df_positive_tweets)>len(df_negative_tweets) :
        return "confiant"
    else :
        return "prudent"


analyse_sentiment_bitcoin()