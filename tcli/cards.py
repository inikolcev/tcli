import requests
import json
import logging

from tcli.constants import API_KEY, API_TOKEN, API_URL
from tcli.lists import get_list_id



def create_card(name, description, board_name, list_name):

    headers = {
       "Accept": "application/json"
    }

    query = {
       'key': API_KEY,
       'token': API_TOKEN,
       'idList': get_list_id(board_name, list_name),
       'name': name,
       'desc': description
    }

    response = requests.request("POST", API_URL + '/cards', headers=headers, params=query)
    print("Card created!")
