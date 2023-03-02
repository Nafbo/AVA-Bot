import requests
import json
import time

def check_dxy_trend():
    # API endpoint pour récupérer les données sur l'indice DX
    url = "https://www.alphavantage.co/query?function=DX&symbol=IBM&interval=daily&time_period=10&apikey=VMX2PEHMPL2NR42N"

    # initialisation des listes de valeurs et de dates
    values = []
    dates = []

    # récupération des 5 dernières valeurs de l'indice DX
    for i in range(5):
        # Requête API pour récupérer les données sur l'indice DX
        response = requests.get(url)

        # Analyse de la réponse JSON
        data = json.loads(response.text)

        # Récupération de la dernière valeur pour l'indice DX
        latest_value = float(data["Technical Analysis: DX"][list(data["Technical Analysis: DX"].keys())[0]]["DX"])
        values.append(latest_value)

        # Récupération de la date de la dernière valeur
        latest_date = list(data["Technical Analysis: DX"].keys())[0]
        dates.append(latest_date)

        # attendre 24 heures avant de récupérer la valeur suivante
        time.sleep(24 * 60 * 60)

    # calcul de la tendance en comparant la dernière valeur à la moyenne des 4 précédentes
    last_value = values[-1]
    avg_last_4_values = sum(values[:-1]) / 4
    trend = "HAUSSE" if last_value > avg_last_4_values else "BAISSE"
    print(f"La tendance actuelle de l'indice DX est à la {trend} ({last_value:.2f} vs {avg_last_4_values:.2f})")
    return print(trend)
    
check_dxy_trend()