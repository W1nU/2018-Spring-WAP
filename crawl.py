import requests as r
import json
from datetime import *
from pprint import pprint

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

def make_time_for_use(flag):
    if flag == 0:
        time_now = datetime.now()
        date_for_use = (time_now - timedelta(days = 1)).strftime("%Y%m%d") if time_now.strftime("%H") == '00' and int(time_now.strftime("%M")) < 40 else date.today().strftime("%Y%m%d")

        if int(time_now.strftime("%H")) == 0 and int(time_now.strftime("%M")) < 40:
            basetime = '2300'
        elif int(time_now.strftime("%M")) >= 40:
            basetime = time_now.strftime("%H00")
        else:
            basetime = (time_now - timedelta(hours = 1)).strftime("%H") + '00'

        return date_for_use, basetime

    elif flag == 1:
        time_now = datetime.now()
        timetable = ['0200','0500','0800','1100','1400','1700','2000','2300']
        date_for_use =

        return date_for_use,basetime

def get_weather_forecast():
    date_for_use, basetime = make_time_for_use(1)
    print(date_for_use, basetime)
    raw = r.get(f"http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastSpaceData?ServiceKey=8dWQmx%2BNiHDmMCfGwZXFIVYPWv807wuz5H%2FE9GLP42G3Al662%2B1vgdjKnM3vPBO65garXv%2BCyBTu5oGKgCmZwg%3D%3D&base_date={date_for_use}&base_time={basetime}&nx=98&ny=75&_type=json")

    pprint(raw.content)

def get_weather_now():
    weather_info = {}
    date_for_use, basetime = make_time_for_use(0)

    raw = r.get(f"http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastGrib?ServiceKey=8dWQmx%2BNiHDmMCfGwZXFIVYPWv807wuz5H%2FE9GLP42G3Al662%2B1vgdjKnM3vPBO65garXv%2BCyBTu5oGKgCmZwg%3D%3D&base_date={date_for_use}&base_time={basetime}&nx=98&ny=75&pageNo=1&numOfRows=10&_type=json")
    weather_info_raw = extract_from_json(raw.content)

    for info in weather_info_raw:
        if info['category'] in decoding_codes.keys():
            weather_info[decoding_codes[info['category']]] = info['obsrValue']

        elif info['category'] in decoding_codes_2layer.keys():
            weather_info[decoding_codes_2layer[info['category']][0]] = decoding_codes_2layer[info['category']][1][str(info['obsrValue'])]

    return weather_info, date_for_use, basetime
