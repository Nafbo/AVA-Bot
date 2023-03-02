from pytrends.request import TrendReq

def average_trend():
    '''Using of the google trend to know the searches carried out around the world and see if there are searches related to bitcoin

    
        Returns:
        Return(String): vogue or not_vogue whether bitcoin is currently trending worldwide

    '''
    keywords = ["Bitcoin","blockchain","crypto-monnaie","transaction", "décentralisation"]
    period = 'today 1-m'
    # Initialiser l'objet TrendReq avec vos informations de connexion Google
    pytrends = TrendReq(hl='fr-FR', tz=0)
    
    # Définir les termes de recherche et la période
    kw_list = keywords
    pytrends.build_payload(kw_list, timeframe=period)

    # Récupérer les données de tendance
    trends_data = pytrends.interest_over_time()

    # Calculer la moyenne des tendances pour la période sélectionnée
    avg_trend = trends_data.mean().mean()

    # Retourner la moyenne des tendances
    
    if avg_trend > 50:
        return "vogue"
    else:
        return "pas_vogue"
