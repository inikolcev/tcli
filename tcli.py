#!/usr/bin/env python3
import argparse
import os
import sys
import logging
import csv

from tcli.lists import get_list_id
from tcli.cards import create_card
from tcli.constants import API_KEY, API_TOKEN, API_URL


def parse_args():
    parser = argparse.ArgumentParser(description='Trello card creater')
    parser.add_argument("-b", "--board", default=None, help="Trello board to use", required=False)
    parser.add_argument("-l", "--list", default=None, help="In what list to create the card", required=False)
    parser.add_argument("-n", "--name", default=None, help="Name of the new card", required=False)
    parser.add_argument("-d", "--description", default=None, help="Optional description for the new card", required=False)
    parser.add_argument("-c", "--csv", default=None, help="Load card from a CSV file", required=False)
    args = parser.parse_args()
    return args

def main():
    args = parse_args()
    logging.basicConfig(format='%(levelname)s:%(message)s')

    if not API_KEY or not API_TOKEN:
        logging.error("Both API_KEY and API_TOKEN environment variables need to be defined!")
        sys.exit(1)

    if args.csv:
        with open(args.csv, "r") as csv_file:
            for row in csv.reader(csv_file, delimiter=','):
                board = row[0]
                board_list = row[1]
                card_name = row[2]
                card_desc = row[3]

                try:
                    create_card(card_name, card_desc, board, board_list)
                except Exception as e:
                    logging.error('Failed to create the card: '+ str(e))

    elif args.name and args.description and args.board and args.list:
        create_card(args.name, args.description, args.board, args.list)
    else:
        sys.exit("Provide either a CSV file or (name, description, board and list).")



if __name__ == "__main__":
    main()
