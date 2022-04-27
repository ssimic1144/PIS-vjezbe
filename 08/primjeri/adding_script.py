import requests
from datetime import datetime, timedelta
import random

for i in range(1,10):
    req_json = {
            "cijena":round(random.uniform(30,180),2),
            "datum":str(datetime.now() + timedelta(days=i))
            }
    r = requests.post("http://127.0.0.1:8080/api/add", json=req_json)
    
    print(r.json())
