#!/usr/bin/env python3
# -*- encoding: utf-8

from telethon.sync import TelegramClient
import json
import logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.DEBUG)

# Use your own values from my.telegram.org
api_id = 12345
api_hash = '0123456789abcdef0123456789abcdef'
phone = input("Enter your phone number with country code (like +919999999999): ")

# The first parameter is the .session file name (absolute paths allowed)
with TelegramClient(phone, api_id, api_hash) as client:
    client.send_message('me', 'Hello, successfully logged in using python client script!')
    
    dialogs = client.get_dialogs()
    
    groups = []
    channel = []
    for dialog in dialogs:
        if dialog.is_group() and not dialog.is_channel():
            groups.append(dialog)
        elif dialog.is_channel():
            channel.append()
    users = {}
    for group in groups:
        users[group.title] = client.get_participants(group)
    
    for channel in channels:
        users[channel.title] = client.get_participants(channel)
    
    with open("users.json", "w") as fp:
        json.dump(users, fp, separators=(',', ':'), indent=4)
    
    client.run_until_disconnected()
