import requests
import logging
import sys

from tcli.constants import API_KEY, API_TOKEN, API_URL
from tcli.boards import get_board_id



def get_list_id(board_name, list_name):
    """
    There is no api call that we can use to get
    list ID by providing a list name.
    So we need to search the provided board for available lists
    and extract the ID from the right list.
    """

    headers = {
       "Accept": "application/json"
    }

    query = {
       'key': API_KEY,
       'token': API_TOKEN
    }

    board_id = get_board_id(board_name)

    response = requests.request("GET", API_URL + f'/boards/{board_id}/lists',
                                headers=headers, params=query)

    for board_lists in response.json():
        if board_lists['name'] == list_name:
            return board_lists['id']
    raise ValueError("The list was not found in the specified board!")
