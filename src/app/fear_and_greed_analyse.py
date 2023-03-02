import requests
import time

def check_fng_index():
    
    url = "https://api.alternative.me/fng/"
    response = requests.get(url)
    data = response.json()

    fng_index = int(data["data"][0]["value"])

    if fng_index <= 25:
        return "rouge"
    elif fng_index >= 75:
        return "vert"
    else:
        return "neutre"

        #time.sleep(24 * 60 * 60)
check_fng_index()
