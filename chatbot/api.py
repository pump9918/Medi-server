# chatbot/api.py

import requests

def get_chatgpt_response(message):
    response = requests.post(
        'https://api.openai.com/v1/chat/completions',  # URL 변경
        headers={
            'Authorization': 'Bearer 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',
            'Content-Type': 'application/json'
        },
        json={
            'model': 'gpt-3.5-turbo',  # 모델 지정 (예시)
            'messages': [{'role': 'user', 'content': message}]
        }
    )
    return response.json()
