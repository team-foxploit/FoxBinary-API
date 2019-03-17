from websocket import create_connection
import json

y = {}

def on_open(ws):
    json_data = json.dumps({'ticks':'R_100'})
    ws.send(json_data)

def on_message(ws, message):
    print('ticks update: %s' % message)
    # y = json.loads(message)
    # print(y)
    # return [message[key] for key in sorted(message.keys())]

def run():
    apiUrl = "wss://ws.binaryws.com/websockets/v3?app_id=1089"
    # ws = websocket.WebSocketApp(apiUrl, on_message = on_message, on_open = on_open)
    # ws.run_forever()
    ws = create_connection(apiUrl)
    while(1):
        on_open(ws)
        result =  ws.recv()
        print("Received '%s'" % result)
        return json.loads(result)



# print("Sending 'Hello, World'...")
# print("Sent")
# print("Receiving...")
# ws.close()
