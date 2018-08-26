import requests as r
from bs4 import BeautifulSoup as bs
import json
from datetime import *
import pprint

date_today = date.today().strftime("%Y%m%d")

def get_weather_forecast():
    raw = r.get(f"http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastSpaceData?ServiceKey=8dWQmx%2BNiHDmMCfGwZXFIVYPWv807wuz5H%2FE9GLP42G3Al662%2B1vgdjKnM3vPBO65garXv%2BCyBTu5oGKgCmZwg%3D%3D&base_date={date_today}&base_time=0500&nx=98&ny=75&_type=json")
    weather_dict = json.loads(raw.content)
    weather_info = weather_dict['response']['body']['items']['item']
    #pprint.pprint(weather_info)
    pprint.pprint(weather_dict)

def get_weather_now():
    raw = r.get("http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastGrib?ServiceKey=8dWQmx%2BNiHDmMCfGwZXFIVYPWv807wuz5H%2FE9GLP42G3Al662%2B1vgdjKnM3vPBO65garXv%2BCyBTu5oGKgCmZwg%3D%3D&base_date=20180826&base_time=0600&nx=98&ny=75&pageNo=1&numOfRows=1&_type=json")
    weather_dict = json.loads(raw.content)
    pprint.pprint(weather_dict)

#get_weather_forecast()
get_weather_now()
