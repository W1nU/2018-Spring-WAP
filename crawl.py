import requests as r
import json
from datetime import *
from pprint import pprint

date_today = date.today().strftime("%Y%m%d")

decoding_codes = {'T1H' : '기온',
                  'RN1' : '1시간 강수량',
                  'REH' : '습도',
                  'VEC' : '풍향',
                  'WSD' : '풍속'}
#2중 구조를 가지는 코드들
decoding_codes_2layer = {'SKY' : ['구름', { '1' : '맑음',
                                           '2' : '구름조금',
                                           '3' : '구름많음',
                                           '4' : '흐림'}],
                         'PTY' : ['강수', { '0' : '비 안내림',
                                           '1' : '비',
                                           '2' : '비/눈',
                                           '3' : '눈'}],
                         'LGT' : ['낙뢰', { '0' : '낙뢰 없음',
                                           '1' : '낙뢰 있음'}]}
def extract_from_json(response):
    weather_dict = json.loads(response)
    return weather_dict['response']['body']['items']['item']

def get_weather_forecast():
    raw = r.get(f"http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastSpaceData?ServiceKey=8dWQmx%2BNiHDmMCfGwZXFIVYPWv807wuz5H%2FE9GLP42G3Al662%2B1vgdjKnM3vPBO65garXv%2BCyBTu5oGKgCmZwg%3D%3D&base_date={date_today}&base_time=0500&nx=98&ny=75&_type=json")
    #weather_info = extract_from_json(raw.content)
    #pprint.pprint(weather_info)
    pprint(weather_info)

def get_weather_now():
    weather_info = []

    raw = r.get(f"http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastGrib?ServiceKey=8dWQmx%2BNiHDmMCfGwZXFIVYPWv807wuz5H%2FE9GLP42G3Al662%2B1vgdjKnM3vPBO65garXv%2BCyBTu5oGKgCmZwg%3D%3D&base_date={date_today}&base_time=0600&nx=98&ny=75&pageNo=1&numOfRows=10&_type=json")
    weather_info_raw = extract_from_json(raw.content)

    for info in weather_info_raw:
        if info['category'] in decoding_codes.keys():
            weather_info.append({decoding_codes[info['category']] : info['obsrValue']})

        elif info['category'] in decoding_codes_2layer.keys():
            info = {decoding_codes_2layer[info['category']][0] : decoding_codes_2layer[info['category']][1][str(info['obsrValue'])]}
            weather_info.append(info)

    return weather_info
