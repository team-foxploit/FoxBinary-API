import websocket
from websocket import create_connection
import time, csv, json 

COUNT = 5000

data = {}
fh = open("result.csv", "w")

def on_open(ws):

    old_req = {
        'ticks_history': 'R_50',
        'end': 'latest',
        'start': 1,
        'style': 'ticks',
        'adjust_start_time': 1,
        'count': COUNT
    }

    req = {
        'ticks_history': 'R_50',
        'end': 'latest',
        'start': 1,
        'style': 'ticks',
        'subscribe': 1,
        'adjust_start_time': 1,
        'count': COUNT
    }

    json_data = json.dumps(req)
    ws.send(json_data)

def on_message(ws, message):
    y = json.loads(message)
    if (y['msg_type'] == "history"):
        prices = y['history']['prices']        
        times = y['history']['times']
        with open('result.csv', mode='w', newline='') as data_file:
            data_writer = csv.writer(data_file,  delimiter=',', quotechar='"', quoting=csv.QUOTE_NONE)
            data_writer.writerow(['date_time', 'price_value', 'trading_state'])
            for i in range(len(prices)):
                price_i = float(prices[i])
                time_i = time.strftime("%d-%b-%Y %H:%M:%S", time.localtime(int(times[i])))
                state_i = {True: "rise", False: "fall"} [price_i <= float(prices[i+5])]
                data[time_i] = price_i
                data_writer.writerow([time_i, price_i, state_i])
        print(data)
    elif(y['msg_type'] == "tick"):
        # tick : {ask, bid, quote, epoch}
        quote_i = y['tick']['bid']
        epoch_i = y['tick']['epoch']
        print(quote_i, epoch_i)


apiUrl = "wss://ws.binaryws.com/websockets/v3?app_id=1089"
ws = websocket.WebSocketApp(apiUrl, on_message = on_message, on_open = on_open)
ws.run_forever()

'''
{
  "echo_req": {
    "adjust_start_time": 1,
    "count": 10,
    "end": "latest",
    "start": 1,
    "style": "ticks",
    "ticks_history": "R_50"
  },
  "history": {
    "prices": [
      "273.2754",
      "273.2777",
      "273.3058",
      "273.3348",
      "273.2416",
      "273.2197",
      "273.2240",
      "273.2314",
      "273.1922",
      "273.2336"
    ],
    "times": [
      "1554568044",
      "1554568046",
      "1554568048",
      "1554568050",
      "1554568052",
      "1554568054",
      "1554568056",
      "1554568058",
      "1554568060",
      "1554568062"
    ]
  },
  "msg_type": "history"
}

{
  "echo_req": {
    "ticks": "R_50"
  },
  "msg_type": "tick",
  "subscription": {
    "id": "309f8394-bc39-edd9-81aa-ac61c46b3b5c"
  },
  "tick": {
    "ask": "273.3588",
    "bid": "273.3188",
    "epoch": 1554568530,
    "id": "309f8394-bc39-edd9-81aa-ac61c46b3b5c",
    "quote": "273.3388",
    "symbol": "R_50"
  }
}

'''