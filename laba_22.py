import requests

# вводим город
s_city = input("Введите город:")
# указываемсвой appid из аккаунта
appid = "1773f4cd02f0155e89ef44e8cca30c5b"

# извлекаем данные с сайта
res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                   params={'q': s_city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
# декодируем информацию с сервера
data = res.json()

# выводим необходимые параметры
print("Город:", s_city)
print("Погодные условия:", data['weather'][0]['description'])
print("Температура:", data['main']['temp'])
print("Минимальная температура:", data['main']['temp_min'])
print("Максимальная температура", data['main']['temp_max'])
print("Скорость ветра:", data['wind']['speed'])
print("Видимость:", data['visibility'])



# извлекаем данные с сайта за неделю
res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
params={'q': s_city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()

# выводим нужные нам значения
print("")
print("~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Прогноз погоды на неделю:")
print("~~~~~~~~~~~~~~~~~~~~~~~~~")
print('')
for i in data['list']:
    print("Дата <", i['dt_txt'], "> \r\nТемпература <", '{0:+3.0f}'.format(i['main']['temp']), "> \r\nПогодныеусловия <", i['weather'][0]['description'], "> \r\nСкорость ветра <", i['wind']['speed'], "> \r\nВидимость <", i['visibility'])
    print("________")






