import requests
import datetime
from config import tg_bot_token, token_api
from aiogram import Bot, types

import aiogram


bot = Bot(token=tg_bot_token)
dp = aiogram.Dispatcher(bot)
@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply(", скажи любой город и я дам погоду")

@dp.message_handler()
async def get_weather(message: types.Message):
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
            f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={token_api}&units=metric"
        )
        data = r.json()

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

        await message.reply(f"**{datetime.datetime.now().strftime('%Y-%m-%h %H:%M')}**\n"
              f"Каланын аты или Названия города: {city} каласы\nТемпература или Ауа райы: {cur_weather} градус {wd}\n"
              f"Влажность немесе : {humidity}\n"
              f'Давление немесе Кысым: {pressure}\n'
              f'Скорость ветер немесе Жел жылдамдыгы: {wind}\n'
              f'Время расхода солнце немесе Тан ату уакыты: {sunrise_timestamp}\n'
              f'Спасибо за использования GakonWeather\n'
              f''
              )


    except:
        await message.reply("\U00002620 Неправильный название города\U00002620")

if __name__ == '__main__':
    aiogram.executor.start_polling(dp)