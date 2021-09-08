# -*- coding: UTF8 -*-
import requests
import os
from dotenv import load_dotenv, find_dotenv


class BotHandler:
    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)

    #url = "https://api.telegram.org/bot<token>/"

    def get_updates(self, offset=0, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text, 'parse_mode': 'HTML'}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def get_first_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[0]
        else:
            last_update = None

        return last_update


# We load the dotenv library
load_dotenv(find_dotenv())

token = os.getenv('TOKEN')      # Your bot's TOKEN
base_bot = BotHandler(token)    # Bot name


def main():
    new_offset = 0
    print('Bot now runing...')

    while True:
        all_updates = base_bot.get_updates(new_offset)

        if len(all_updates) > 0:
            for current_update in all_updates:
                first_update_id = current_update['update_id']

                # This line cheeks if the current_update doesn't have a message or if the message dosen't have text. If so it discards it
                if 'message' not in current_update or 'text' not in current_update['message']:
                    new_offset = first_update_id + 1
                # Else, it awsers the message
                else:
                    first_chat_text = current_update['message']['text']
                    first_chat_id = current_update['message']['chat']['id']
                    first_chat_name = current_update['message']['from']['first_name']

                    if first_chat_text == 'Hi':
                        base_bot.send_message(
                            first_chat_id, 'Morning ' + first_chat_name)
                        new_offset = first_update_id + 1
                    else:
                        base_bot.send_message(
                            first_chat_id, 'How are you doing '+first_chat_name)
                        new_offset = first_update_id + 1


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
