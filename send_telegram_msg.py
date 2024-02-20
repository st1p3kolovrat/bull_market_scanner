import requests


def send_telegram_msg(message):
    bot_token = "{YOUR_BOT_TOKEN}"
    chat_id = "{YOUR_CHAT_ID}"
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "parse_mode": "HTML",
        "text": message
    }
    response = requests.post(url, json=payload)
    return response
