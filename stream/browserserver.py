#!/usr/bin/env python

# WS server that sends messages at random intervals

'''
import asyncio
import datetime
import random
import websockets

async def time(websocket, path):
    while True:
        now = datetime.datetime.utcnow().isoformat() + 'Z'
        await websocket.send(now)
        await asyncio.sleep(random.random() * 3)

start_server = websockets.serve(time, '127.0.0.1', 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
'''


import websocket
from websocket import create_connection
import json

y = {}

def on_open(ws):
    json_data = json.dumps({'ticks':'R_100'})
    ws.send(json_data)

def on_message(ws, message):
    print('ticks update: %s' % message)
    y = json.loads(message)
    print(y)
    # return [message[key] for key in sorted(message.keys())]

apiUrl = "wss://ws.binaryws.com/websockets/v3?app_id=1089"
ws = websocket.WebSocketApp(apiUrl, on_message = on_message, on_open = on_open)
ws.run_forever()