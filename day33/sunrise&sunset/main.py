import requests
from datetime import datetime

MY_LATITUDE=12.971599
MY_LONGITUDE=77.594566

parameters={
    "lat":MY_LATITUDE,
    "lng":MY_LONGITUDE,
    "formatted":0
}

response=requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
data=response.json()

sunrise=data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset=data["results"]["sunset"].split("T")[1].split(":")[0]

time_now=datetime.now()

print(f"The sunrise time is {sunrise}")
print(f"The sunset time is {sunset}")
print(f"The current time is {time_now.hour}")