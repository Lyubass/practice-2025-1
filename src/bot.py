import telebot
import requests

bot = telebot.TeleBot("7615771732:AAEys1OYG2bJmw4l1mq6hW_y5KTy3EYENhE")

@bot.message_handler(commands=['start'])
def ask_city(message):
    bot.send_message(message.from_user.id, 'Введите название города, для которого хотите узнать погоду.')

@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text
    api_key = 'e0ea790c30465c6d097b7b535681ad28'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=ru&appid={api_key}'
    
    try:
        weather_data = requests.get(url)
        weather_data.raise_for_status()
        weather_data = weather_data.json()
    
        if weather_data.get('cod') != 200:
            bot.send_message(message.from_user.id, 'Город не найден. Пожалуйста, попробуйте снова.')
            return
    
        temperature = round(weather_data['main']['temp'])
        temperature_feels = round(weather_data['main']['feels_like'])
    
        w_now = f'Сейчас в городе {city} {temperature} °C'
        w_feels = f'Ощущается как {temperature_feels} °C'
    
        bot.send_message(message.from_user.id, w_now)
        bot.send_message(message.from_user.id, w_feels)
    
    except requests.exceptions.RequestException as e:
        bot.send_message(message.from_user.id, 'Произошла ошибка при получении данных о погоде: ' + str(e))

bot.polling()