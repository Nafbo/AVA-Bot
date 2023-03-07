import requests
TOKEN = '6091261455:AAEQ6ZZlLqkLYyNOOZkDpujQJ3dyLjAfzj8'
chat_id = "6210537537"
message_openLongPosition = ("Bonjour, 👋\n\n"
            "🚨 Je suis ravi de vous informer que j'ai ouvert une nouvelle position pour vous.🚨 \n\n"
            "Voici les détails de la transaction : 📈 \n\n"

            "       Crypto : \n"
            "       Type de position : \n"
            "       Usd Investit : \n"
            "       Prix d'ouverture : \n"
            "       Stop loss : \n"
            "       Take profit : \n\n"

            "Je surveillerai attentivement l'évolution de cette position et vous informerai de tout changement important. 📣\n\n"

            "Cordialement,\n"
            "Votre AVA Bot de trading. 🤖")

message_openShortPosition = ("Bonjour, 👋\n\n"
            "🚨 Je suis ravi de vous informer que j'ai ouvert une nouvelle position pour vous.🚨 \n\n"
            "Voici les détails de la transaction : 📉 \n\n"

            "       Crypto : \n"
            "       Type de position : \n"
            "       Usd Investit : \n"
            "       Prix d'ouverture : \n"
            "       Stop loss : \n"
            "       Take profit : \n\n"

            "Je surveillerai attentivement l'évolution de cette position et vous informerai de tout changement important. 📣\n\n"

            "Cordialement,\n"
            "Votre AVA Bot de trading. 🤖")

message_closeShortPosition = ("Bonjour, 👋\n\n"
            "🚨 Je suis ravi de vous informer que j'ai fermé une position pour vous.🚨 \n\n"
            "Voici les détails de la transaction : 📉 \n\n"

            "       Crypto : \n"
            "       Type de position : \n"
            "       Fermeture par: \n"
            "       Performance : \n"
            "       Usd Gagné/Perdu: \n"
            "       Prix de fermeture : \n\n"
            
            "Je surveillerai attentivement l'évolution du marché et je vous informerai d'une prochaine ouverture de position. 📣\n\n"

            "Cordialement,\n"
            "Votre AVA Bot de trading. 🤖")

message_closeLongPosition = ("Bonjour, 👋\n\n"
            "🚨 Je suis ravi de vous informer que j'ai fermé une position pour vous.🚨 \n\n"
            "Voici les détails de la transaction : 📈 \n\n"

            "       Crypto : \n"
            "       Type de position : \n"
            "       Fermeture par: \n"
            "       Performance : \n"
            "       Usd Gagné/Perdu: \n"
            "       Prix de fermeture : \n\n"
            
            "Je surveillerai attentivement l'évolution du marché et je vous informerai d'une prochaine ouverture de position. 📣\n\n"

            "Cordialement,\n"
            "Votre AVA Bot de trading. 🤖")


url = "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}".format(TOKEN, chat_id, message_closeShortPosition)

print(requests.get(url).json())