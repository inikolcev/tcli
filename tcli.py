#!/usr/bin/env python3
import argparse
import os
import sys
import logging

from tcli.lists import get_list_id
from tcli.cards import create_card
from tcli.constants import API_KEY, API_TOKEN, API_URL


def parse_args():
    parser = argparse.ArgumentParser(description='Trello card creater')
    parser.add_argument("-b", "--board", help="Trello board to use", required=True)
    parser.add_argument("-l", "--list", help="In what list to create the card", required=True)
    parser.add_argument("-n", "--name", help="Name of the new card", required=True)
    parser.add_argument("-d", "--description", help="Optional description for the new card", required=True)
    args = parser.parse_args()
    return args

def main():
    args = parse_args()
    logging.basicConfig(format='%(levelname)s:%(message)s')

    if not API_KEY or not API_TOKEN:
        logging.error("Both API_KEY and API_TOKEN environment variables need to be defined!")
        sys.exit(1)

    create_card(args.name, args.description, args.board, args.list)


if __name__ == "__main__":
    main()
