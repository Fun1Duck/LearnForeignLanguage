import requests


# Адрес локального сервера
url = "http://localhost:5000/translate"

# Данные для перевода
data = {
    "q": "Hello, how are you?",
    "source": "auto",      # Автоопределение языка
    "target": "ru",        # Перевод на русский
    "format": "text",      # Формат текста
    "alternatives": 3      # Показать 3 варианта перевода
}

# Заголовки
headers = {
    "Content-Type": "application/json"
}

# Отправка запроса
response = requests.post(url, json=data, headers=headers)

# Вывод ответа
if response.status_code == 200:
    result = response.json()
    print("Перевод:", result["translatedText"])
    print("Альтернативы:", result.get("alternatives", []))
else:
    print("Ошибка:", response.status_code)
    print(response.text)