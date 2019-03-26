import time
import socket
import pickle
import websocket
from websocket import create_connection
import json

HEADER_SIZE = 100

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 6000))
s.listen(5)

def on_open(ws):
    json_data = json.dumps({'ticks':'R_100'})
    ws.send(json_data)

def on_message(ws, message):
    # print('ticks update: %s' % message)
    # data = {
    #     "name": "Kamal",
    #     "email": "kamal@yahoo.com"
    # }
    msg = pickle.dumps(message)
    # print(msg)
    msg = bytes(f'{len(msg):<{HEADER_SIZE}}', "utf-8") + msg
    clientSocket.send(msg)
    # y = json.loads(message)
    # print(y)
    # return [message[key] for key in sorted(message.keys())]


while True:
    clientSocket, address = s.accept()
    print(f"connection from {address} has been established!")

    apiUrl = "wss://ws.binaryws.com/websockets/v3?app_id=1089"
    ws = websocket.WebSocketApp(apiUrl, on_message = on_message, on_open = on_open)
    ws.run_forever()
    # welcome_msg = "Welcome to the server!"
    # data = {
    #     "name": "Kamal",
    #     "email": "kamal@yahoo.com"
    # }
    # msg = pickle.dumps(data)
    # print(msg)
    # msg = bytes(f'{len(msg):<{HEADER_SIZE}}', "utf-8") + msg
    # clientSocket.send(msg)
