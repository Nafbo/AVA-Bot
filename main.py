import requests as rq
import pandas as pd

url = "https://u3ruvos9xf.execute-api.eu-west-1.amazonaws.com/items"
r = rq.get(url).json()
df  = pd.DataFrame(r)
df = df.sort_values('user_name')
print(df[-4:]['sentiment_marche'])