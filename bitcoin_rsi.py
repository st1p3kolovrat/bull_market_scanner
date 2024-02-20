import requests
import logging
from jsonpath_ng import parse


def bitcoin_rsi():
    endpoint_url = "https://api.taapi.io/rsi"
    query_params = {
        'secret': '{YOUR_SECRET}',
        'exchange': 'binance',
        'symbol': 'BTC/USDT',
        'interval': '1w'
    }
    response = requests.get(url=endpoint_url, params=query_params)
    json_path_expression = parse("$.value")
    btc_rsi_list = [match.value for match in json_path_expression.find(response.json())]
    btc_rsi_value = float(btc_rsi_list[0])
    # Round number to 3 decimal points
    btc_rsi = round(btc_rsi_value, 3)
    logging.info(f"Bitcoin(1W) RSI: {btc_rsi}")
    return btc_rsi
