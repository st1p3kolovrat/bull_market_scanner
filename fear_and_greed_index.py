import requests
import logging
from jsonpath_ng import parse


def fear_and_greed_index():
    endpoint_url = "https://api.alternative.me/fng/"
    greed_response = requests.get(endpoint_url)
    json_path_expression = parse("$.data..value")
    greed_index_list = [match.value for match in json_path_expression.find(greed_response.json())]
    greed_index_value = int(greed_index_list[0])
    logging.info(f"Current fear and greed index is: {greed_index_value}")
    return greed_index_value
