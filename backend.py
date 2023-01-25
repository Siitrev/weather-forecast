from key import API_KEY
from datetime import date
import requests

def get_data(place, forecast_days):
    
    api_call = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&cnt={forecast_days*8}&appid={API_KEY}&units=metric"
    res = requests.get(api_call)
    data = res.json()
    
    return data["list"]
