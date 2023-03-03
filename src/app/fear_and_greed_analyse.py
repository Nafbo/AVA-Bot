import requests
import time



def check_fng_index():
    '''Retrieves information from the fear and greed index
    
        Returns:
    
        Return(String) green (>=75), neutral (between 25 and 75) or red (<=25)
    '''
    
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
