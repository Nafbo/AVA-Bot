import tweepy
import pandas as pd
import openai
import random
import re
import warnings
warnings.filterwarnings("ignore")

def chatGPT():
    consumer_key = "Tj8wId3oOGzdWekvZb1iIV0jG"
    consumer_secret = "ejwWuGual0tIJRUGM3sLGAzkkWeqeO2uqari7OBJHGo5S9xlmc"
    access_token = "922523786766901249-OGfv3s7U7DDrmHEPPourORXDKF3lIzk"
    access_token_secret = "jXaMSRgzJOdmT8BxRLujbHc3NHfvMZj0xSEkE8JyWs4cs"
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    
    influencers = ['FranceCryptos', 'CryptoMatrix2', 'CoinDesk', 'CryptoSlate', 'MessariCrypto']

    df_tweets = pd.DataFrame(columns=['text'])

    for influencer in influencers:
        nombre_aleatoire = random.randint(3, 5)
        tweets = api.user_timeline(screen_name=influencer, count=nombre_aleatoire)
        for tweet in tweets:
            df_tweets = df_tweets.append({'text': tweet.text}, ignore_index=True)
    df_tweets.text = df_tweets.text.str.replace('@\w+', '')
    df_tweets.text = df_tweets.text.str.replace('http\S+', '')
    texte_complet = ''.join(df_tweets.text.tolist())
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               "]+", flags=re.UNICODE)
    texte_complet = emoji_pattern.sub(' ', texte_complet)
    texte_complet = texte_complet.strip()
    texte_complet = texte_complet.replace("\n", "")
    openai.api_key = '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'
    
    prompt = ("Fais-moi un résumé de ces tweets, en enlevant tout ce qui ne te parés pas intéressant et n'est pas complet:"+texte_complet)
    completion = openai.Completion.create(
        engine = 'text-davinci-002',
        prompt=prompt,
        max_tokens=200,
        n=3,
        stop=None,
        temperature=0,
        presence_penalty = 1,
    )
    new_text = str(completion.choices[0].text+completion.choices[1].text+completion.choices[2].text)   
    
    phrase = ['You are a specialist in cryptocurrency trading, with the help of the following articles on the actuality of cryptocurrency, give me the feeling of the current market: ',
              "As an expert in cryptocurrency trading, I'm looking to get a pulse on the current market trends. Could you summarize the following text on the latest happenings in the crypto world? ",
              "I'm hoping to tap into your expertise as a specialist in cryptocurrency trading. Could you provide me with some insights on the current state of the market, backed up by articles on the latest cryptocurrency news? ", 
              "With your knowledge and experience in cryptocurrency trading, I'm eager to hear your thoughts on the current state of the market. Could you witre a summarize that highlight the latest trends and developments in the world of crypto? "]
    prompt2 = str(random.choice(phrase) + new_text)
    prompt2 = prompt2.replace("\n", "")

    completion1 = openai.Completion.create(
        engine = 'text-davinci-002',
        prompt=prompt2,
        max_tokens=2000,
        n=1,
        stop=None,
        temperature=0.3,
        presence_penalty = 1
        )
    phrase2 = ["If this text is has not a correct syntax, semantics, and pragmatics, rewrite this text in a new text, else juste write the following text:",
               "If this text does not have the right syntax, semantics and pragmatics, rewrite this text into a new text, otherwise just write the following text:",
               "If this text does not have the right syntax, semantics and pragmatics, rewrite this text into a new text, otherwise just write the following text:",
               "If this text does not have the right syntax, semantics and pragmatics, rewrite it into a new text, otherwise just write the following text:"]
    prompt3 = str(random.choice(phrase2)+completion1.choices[0].text)
    completion2 = openai.Completion.create(
        engine = 'text-davinci-002',
        prompt=prompt3,
        max_tokens=2000,
        n=1,
        stop=None,
        temperature=0,
        presence_penalty = 1
        )
    
    if len(completion2.choices[0].text) < 50 and len(completion2.choices[0].text) > 5130:
        for influencer in influencers:
            nombre_aleatoire = random.randint(5, 10)
            tweets = api.user_timeline(screen_name=influencer, count=nombre_aleatoire)
            for tweet in tweets:
                df_tweets = df_tweets.append({'text': tweet.text}, ignore_index=True)
        df_tweets.text = df_tweets.text.str.replace('@\w+', '')
        df_tweets.text = df_tweets.text.str.replace('http\S+', '')
        texte_complet = ''.join(df_tweets.text.tolist())
        emoji_pattern = re.compile("["
                                u"\U0001F600-\U0001F64F"  # emoticons
                                u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                "]+", flags=re.UNICODE)
        texte_complet = emoji_pattern.sub(' ', texte_complet)
        texte_complet = texte_complet.strip()
        texte_complet = texte_complet.replace("\n", "")
    
        prompt = ("Fais-moi un résumé de ces tweets, en enlevant tout ce qui ne te parés pas intéressant et n'est pas complet:"+texte_complet)
        completion = openai.Completion.create(
            engine = 'text-davinci-002',
            prompt=prompt,
            max_tokens=200,
            n=3,
            stop=None,
            temperature=0,
            presence_penalty = 1)
        new_text = str(completion.choices[0].text+completion.choices[1].text+completion.choices[2].text)
    
        prompt2 = str(random.choice(phrase) + new_text)
        prompt2 = prompt2.replace("\n", "")

        completion1 = openai.Completion.create(
            engine = 'text-davinci-002',
            prompt=prompt2,
            max_tokens=2000,
            n=1,
            stop=None,
            temperature=0.3,
            presence_penalty = 1
            )
            
        prompt3 = str(random.choice(phrase2)+completion1.choices[0].text)
        completion2 = openai.Completion.create(
            engine = 'text-davinci-002',
            prompt=prompt3,
            max_tokens=2000,
            n=1,
            stop=None,
            temperature=0,
            presence_penalty = 1)
        
    text_final = completion2.choices[0].text.replace("\n", "")
    return(text_final)  

if __name__ == '__main__':
    print(chatGPT())