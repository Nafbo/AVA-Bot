import ccxt
import requests
from pytrends.request import TrendReq



def tendance_bitcoin():
    pytrends = TrendReq(hl='fr-FR', tz=0)

# Définir les termes de recherche et la période
    kw_list = ["Bitcoin","blockchain","crypto-monnaie","transaction", "décentralisation"]
    pytrends.build_payload(kw_list, timeframe='today 1-m')

# Récupérer les données de tendance
    bitcoin_trends = pytrends.interest_over_time()
# Calculer la moyenne des tendances pour la période sélectionnée
    avg_trend = bitcoin_trends.mean()[0]

# Afficher la moyenne des tendances
    if avg_trend > 50:
        return "Le Bitcoin est en vogue avec une moyenne de tendance de", avg_trend
    else:
        return "Le Bitcoin n'est pas en vogue avec une moyenne de tendance de", avg_trend



def get_btc_price():
    # créer une instance de l'échange Binance
    exchange = ccxt.binance()

    # récupérer les données de marché pour BTC/USDT
    ticker = exchange.fetch_ticker('BTC/USDT')

    # extraire le prix actuel
    btc_price = ticker['last']

    # retourner le prix en tant que flottant
    return "Le prix du bitcoin actuellement est de",float(btc_price),"USD"

def get_sentiment():
    
    url = "https://api.alternative.me/fng/"
    response = requests.get(url)
    data = response.json()

    fng_index = int(data["data"][0]["value"])
    if fng_index <= 25:
        return "Le marché est trop dans le rouge. Il est temps d'être prudent."
    elif fng_index >= 75:
        return "Le marché est trop dans le vert. Il est temps d'être vigilant."
    else:
        return "Le marché est actuellement neutre"

# Paires question - réponse
pairs = {
    'comment ça va?': 'Je suis un chatbot, donc je ne ressens pas vraiment les émotions, mais je suis prêt à vous aider !',
    'quel est ton nom?': 'Je suis Leo, votre assistant virtuel.',
    'Qui est AVA?': 'AVA est une équipe de trois jeunes ingénieurs en formation à l ESME SUDRIA qui sont passionés par le monde des cryptomonnaies et la data !',
    'Qui sont ces trois étudiants ingénieurs?':'Mes trois fidèles amis sont Alice Miermon, Victor Bonnafous et Adrian Boyer.',
    'comment fonctionne le bot de trading AVA?':'Le bot utilise différents indicateurs et analyse les sentiments du marché pour pouvoir être le plus juste possible lors d ouverture de positions',
    'quoi de neuf sur le bitcoin actuellement?': tendance_bitcoin(),
    'quel est le prix actuel du bitcoin?': get_btc_price(),
    'quel est le sentiment du marché concernant le bitcoin?': get_sentiment(),
    'aide': 'Je suis là pour vous aider. Vous pouvez écrire un numéro de question et je tacherai de répondre le plus rapidement possible ! Que puis-je faire pour vous ?',
    'au revoir': 'Au revoir !',
}

# Affichage des questions possibles
print("\nBonjour voici Leo, votre Chatbot personnalisé concernant le Bitcoin et les sentiments du marché !\n")
print("\nVeuillez choisir une question parmi les options suivantes : \n")

# Boucle for pour afficher les questions numérotées
for i, question in enumerate(pairs.keys()):
    print(f"{i+1}. {question}")

def get_user_choice():
    while True:
        user_input = input("\nQue voulez-vous savoir? Entrez le numéro correspondant à votre choix : \n")
        try:
            user_input = int(user_input)
        except ValueError:
            print("\nVeuillez entrer un nombre valide.\n")
            continue
        if user_input in range(1, len(pairs)+1):
            question = list(pairs.keys())[user_input-1]
            response = pairs[question]
            print(f"Question : {question}")
            if question == 'quel est le prix actuel du bitcoin?':
                response = get_btc_price()
            if question =='quel est le sentiment du marché concernant le bitcoin?':
                response = get_sentiment()
            if question =='quoi de neuf sur le bitcoin actuellement?':
                response = tendance_bitcoin()
            print(f"Réponse : {response}")
            if question == 'au revoir':
                break
        else:
            print("Veuillez entrer une réponse valide.")
    return response

get_user_choice()
