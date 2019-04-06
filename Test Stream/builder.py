import websocket
from websocket import create_connection
import json



def on_open(ws):
    json_data = json.dumps({'ticks':'R_100'})
    ws.send(json_data)

def on_message(ws, message):
    y = json.loads(message)
    print(y['tick']['quote'])

apiUrl = "wss://ws.binaryws.com/websockets/v3?app_id=1089"
ws = websocket.WebSocketApp(apiUrl, on_message = on_message, on_open = on_open)
ws.run_forever()