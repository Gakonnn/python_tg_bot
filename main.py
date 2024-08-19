import requests
import datetime
from pprint import pprint
from config import token_api

def get_weather(city, token_api):
    code_to_smile = {
        "Clear": 'Ясно \U00002600',
        'Clouds': 'Облачно \U00002601',
        'Rain': 'Дождь \U00002614',
        'Orizzle': 'Дождь \U00002614',
        'Thunderstorm': 'Гроза \U000026A1',
        'Show': 'Снег \U0001F328',
        'Mist': 'Туман \U00001F32B',

    }


    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={token_api}&units=metric"
        )
        data = r.json()
        # pprint(data)

        city = data["name"]
        cur_weather = data['main']['temp']

        weather_description = data['weather'][0]['main']
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = 'Посмотри на улицу и сам узнай'



        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind = data['wind']['speed']
        sunrise_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunrise'])

        print(f"**{datetime.datetime.now().strftime('%Y-%m-%h %H:%M')}**\n"
              f"Каланын аты или Названия города: {city} каласы\nТемпература или Ауа райы: {cur_weather} градус {wd}\n"
              f"Влажность немесе Ылгалдык ебать: {humidity}\n"
              f'Давление немесе Кысым: {pressure}\n'
              f'Скорость ветер немесе Жел жылдамдыгы: {wind}\n'
              f'Время расхода солнце немесе Тан ату уакыты: {sunrise_timestamp}\n'
              f'Спасибо за использования GakonWeather\n'
              f'Маладес GakonWeather колданганына'
              )


    except Exception  as ex:
        print(ex)
        print("Каланын аты неправильный, проверь по бр ЛЕ")

def main():
    city = input("Любой каланын атын айтшы:")
    get_weather(city, token_api)


if __name__ == "__main__":
    main()