import requests
import logging
import sys

from tcli.constants import API_KEY, API_TOKEN, API_URL



def get_board_id(board_name):
    """
    Get board ID by providing a board name
    """

    headers = {
       "Accept": "application/json"
    }

    query = {
       'key': API_KEY,
       'token': API_TOKEN
    }

    response = requests.request("GET", API_URL + '/members/me/boards',
                                headers=headers, params=query)

    for board in response.json():
        if board['name'] == board_name:
            return board['id']
    raise ValueError("The specified board was not found!")
