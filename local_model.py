import requests
import json


# Адрес API
API_URL = "http://127.0.0.1:1234/v1/chat/completions"
# модели: google/gemma-3n-e4b , google/gemma-3-4b , deepseek/deepseek-r1-0528-qwen3-8b , qwen/qwen3-30b-a3b-2507

async def query_lm_studio(messages):
    # Настройки генерации
    data = {
        "model": "qwen/qwen3-30b-a3b-2507",  # Название модели
        "messages": messages,
        "temperature": 0.7,
        "max_tokens": 1024,
        "stream": False
    }

    # Отправляем запрос
    try:
        response = requests.post(API_URL, json=data)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"Ошибка: {e}")
        return f"Ошибка при генерации текста"