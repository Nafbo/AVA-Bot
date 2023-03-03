import tweepy
import time

def analyze_whale_alert_tweets():
    
    '''Using the twitter API to retrieve the latest tweets from an account about whales with a lot of BTC

    
        Returns:
        Return(String): dangerous or very dangerous or normal if there is something concerning BTC

    '''
    # Configuration de l'authentification Twitter
    auth = tweepy.OAuthHandler("88dldRnuq6fLPQKkX8azrCd5p", "WTZDb3JRQUjZVRu6LhQNhIVzoQpZ2Cd2i6ePKnRATeQnBuNx6g")
    auth.set_access_token("1435977329524752387-xa4DXdjkxgYNhbBJbdJZgySGC2YjRy", "CneEP3iDzDhiho3UDhAFjnPTvdUBcVAsluoH574urkINb")

    # Utilisation de l'authentification pour accéder à l'API Twitter
    api = tweepy.API(auth)

    # Récupération des tweets de "whale_alert" contenant le #BTC ou #WBTC
    tweets = api.user_timeline(screen_name="whale_alert", count=200)
    for tweet in tweets:
        if "#BTC" in tweet.text or "#WBTC" in tweet.text:
            # Analyse du tweet pour déterminer s'il est dangereux ou normal
            num_emojis = tweet.text.count("🚨")
            if num_emojis == 2 or num_emojis == 3:
                return "dangereux"
            elif num_emojis > 3 :
                return "très_dangereux"
            else:
                return "normal"

            #text_without_links = tweet.text
            #for url in tweet.entities.get('urls'):
                #text_without_links = text_without_links.replace(url['url'], '')

            # Affichage du tweet en entier avec l'indication de son niveau de danger
            #return f"WHALES : \nTweet suivant, posté le {tweet.created_at},avec {num_emojis} emojis 🚨:\n--> {danger_level}\n--> {text_without_links}\n------------------------\n"
            

    

    # Pause pour ne pas dépasser les limites d'accès à l'API Twitter
    time.sleep(60)
    

    

