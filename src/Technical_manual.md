
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
   pip install pyTelegramBotAPI
   ```
Библиотека `pyTelegramBotAPI` необходима для работы с Telegram API


   ```bash
   pip install requests
   ```
Библиотека `requests` нужна для HTTP-запросов к OpenWeatherMap

2. Подключаем наши библиотеки, в качестве переменной `bot` берем полученный токен в BotFather, пишем функцию для команды `/start`:
```bash
   import telebot
import requests

bot = telebot.TeleBot("7615771732:AAEys1OYG2bJmw4l1mq6hW_y5KTy3EYENhE")

@bot.message_handler(commands=['start'])
def ask_city(message):
    bot.send_message(message.from_user.id, 'Введите название города, для которого хотите узнать погоду.')
   ```
3.


