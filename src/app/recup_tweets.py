import requests
import json
import csv
import datetime

# Remplacez les valeurs ci-dessous par les informations de votre compte Twitter
consumer_key = "88dldRnuq6fLPQKkX8azrCd5p"
consumer_secret = "WTZDb3JRQUjZVRu6LhQNhIVzoQpZ2Cd2i6ePKnRATeQnBuNx6g"


# Créez un jeton d'accès en utilisant vos informations d'identification
bearer_token = requests.post(
    "https://api.twitter.com/oauth2/token",
    auth=(consumer_key, consumer_secret),
    data={"grant_type": "client_credentials"}
).json()["access_token"]

# Définissez l'URL de l'API de recherche de Twitter
url = "https://api.twitter.com/1.1/search/tweets.json"

# Calculate the date 1 month ago
one_month_ago = datetime.datetime.now() - datetime.timedelta(days=30)

# Ouvrez un fichier CSV en mode écriture pour stocker les tweets récupérés
with open("tweets_1_month_ago.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    # Écrivez l'en-tête du fichier CSV
    writer.writerow(["username", "tweet"])

    # Définissez les paramètres de la requête
    params = {
        "q": "bitcoin",
        "lang": "en",
        "result_type": "recent",
        "count": 1000,
        "since_id": one_month_ago.strftime("%Y-%m-%d")
    }

    # Envoyez la requête à l'API de recherche de Twitter
    response = requests.get(
        url,
        params=params,
        headers={"Authorization": f"Bearer {bearer_token}"}
    )

    # Chargez la réponse de l'API en tant que dictionnaire Python
    data = response.json()

    # Parcourez les tweets récupérés et enregistrez-les dans le fichier CSV
    for tweet in data["statuses"]:
        writer.writerow([tweet["user"]["screen_name"], tweet["text"]])
        
        

