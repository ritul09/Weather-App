import datetime as dt
import requests
import json


BASE_URL = 'https://api.openweathermap.org/data/2.5/weather?'
# API_KEY = open('key.txt', 'r').read()
API_KEY = open('wTell_key.txt', 'r').read()


class GetReport:
    def __init__(self, city) -> None:
        self.response = None
        self.url = BASE_URL + 'appid=' + API_KEY + '&q=' + city


    def getResponse(self) -> dict:
        try:
            self.response = requests.get(self.url).json()
            return self.response
        
        except Exception as err:
            self.response = None
            return {'msg': 'Something went wrong!', 'error': err}


    def getDummy(self) -> dict:
        try:
            with open("weather_data_test.json", "r") as outfile:
                self.response = json.load(outfile)
            return self.response
        
        except Exception as err:
            self.response = None
            return {'msg': 'Something went wrong!', 'error': err}


    def kel_to_cel(self, kelvin) -> float:
        cel = kelvin - 273.15
        return cel
    

    def getName(self) -> str:
        return self.response['name']
    

    def getTemp(self) -> float:
        return self.kel_to_cel(self.response['main']['temp'])


    def getFeelslike(self) -> float:
        return self.kel_to_cel(self.response['main']['feels_like'])
    

    def getHumidity(self) -> float:
        return self.response['main']['humidity']


    def getWindspeed(self):
        return self.response['wind']['speed']


    def getDescription(self) -> str:
        return self.response['weather'][0]['description']


    def getSunrise(self) -> str:
        return dt.datetime.utcfromtimestamp(self.response['sys']['sunrise'] + self.response['timezone']).strftime('%Y-%m-%d %I:%M %p')
    

    def getSunset(self) -> str:
        return dt.datetime.utcfromtimestamp(self.response['sys']['sunset'] + self.response['timezone']).strftime('%Y-%m-%d %I:%M %p')


    def getIcon(self) -> str:
        return self.response['weather'][0]['icon']


    def getData(self):
        if self.response is None or self.response['cod'] != 200:
            return {}
        data = {
            'name': f'{self.getName()}',
            'temp': f'{self.getTemp():.2f}',
            'feels_like': f'{self.getFeelslike():.2f}',
            'humidity': f'{self.getHumidity()} %',
            'windspeed': f'{self.getWindspeed()} m/s',
            'description': f'{self.getDescription().capitalize()}',
            'sunrise': f'{self.getSunrise()}',
            'sunset': f'{self.getSunset()}',
            'icon_url': f'https://openweathermap.org/img/wn/{self.getIcon()}.png'
        }
        return data
