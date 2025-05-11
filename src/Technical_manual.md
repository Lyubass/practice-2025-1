
## Техническое руководство по созданию бота

### Шаг 1: Создание бота в Telegram

1. Откройте Telegram и введите в поисковой строке @BotFather
2. Используйте команду /newbot для создания нового бота
3. Запишите полученный токен (он понадобится позже):

![Компьютер](img/BotFather.png)

### Шаг 2: Получение API ключа OpenWeatherMap

1. Зарегистрируйтесь на [OpenWeatherMap](https://openweathermap.org/)
2. Перейдите в раздел API Keys (он находиться в личном кабинете), создайте новый API ключ и сохраните его:

 ![Компьютер](img/key.png)

4. Так же нам понадобится API-запрос для получения данных о погоде по названию города, он находится в разделе API - Built-in API request by city name (копируем первый из 3-х):

 ![Компьютер](img/API.png)


### Шаг 3: Переходим к написанию кода

1. Устанавливаем необходимые библиотеки через терминал:
   
```bash
pip install pyTelegramBotAP
```

Библиотека `pyTelegramBotAPI` необходима для работы с Telegram API

   ```bash
   pip install requests
   ```

Библиотека `requests` нужна для HTTP-запросов к OpenWeatherMap


2. Сам код с комментариями:
```bash
# Подключаем библиотеки
import telebot
import requests

# Создаем объект бота, передавая уникальный токен полученый в BotFather, этот токен связывает ваш код с конкретным ботом в Telegram
bot = telebot.TeleBot("7615771732:AAEys1OYG2bJmw4l1mq6hW_y5KTy3EYENhE") 

# Пишем функцию для комнды /start:
@bot.message_handler(commands=['start'])
def ask_city(message):
    bot.send_message(message.from_user.id, 'Введите название города, для которого хотите узнать погоду.')

# Получаем город от пользователя, формируем запрос к погодному API:
@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text
    api_key = 'e0ea790c30465c6d097b7b535681ad28' # API ключ из OpenWeatherMap
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=ru&appid={api_key}' # Создаём ссылку для запроса погоды

# Получаем данные погоды:    
    try:
        weather_data = requests.get(url) # Отправляем запрос к API погоды
        weather_data.raise_for_status()
        weather_data = weather_data.json() # Преобразуем ответ в удобный формат

  # Проверяем, найден ли город:  
        if weather_data.get('cod') != 200:
            bot.send_message(message.from_user.id, 'Город не найден. Пожалуйста, попробуйте снова.')
            return

    # Если город найден - показываем погоду:  
        temperature = round(weather_data['main']['temp'])
        temperature_feels = round(weather_data['main']['feels_like'])

    # Формируем ответы: 
        w_now = f'Сейчас в городе {city} {temperature} °C'
        w_feels = f'Ощущается как {temperature_feels} °C'

    # Отправляем пользователю:
        bot.send_message(message.from_user.id, w_now)
        bot.send_message(message.from_user.id, w_feels)

# Обрабатываем возможные ошибки:
    except requests.exceptions.RequestException as e:
        bot.send_message(message.from_user.id, 'Произошла ошибка при получении данных о погоде: ' + str(e))

bot.polling()
   ```

### Запуск программы:
1. Сохраняем файл и запускаем код через терминал:
   
```bash
python bot.py
```   
2. Переходим в Telegram и проверяем работу бота:
