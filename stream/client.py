import time
import socket
import pickle

HEADER_SIZE = 100

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 6000))

while True:
    full_msg = b''
    new_msg = True
    while True:
        msg = s.recv(160)
        if new_msg:
            # print(f"new message length: {msg[:HEADER_SIZE]}")
            msg_len = int(msg[:HEADER_SIZE])
            new_msg = False
        
        full_msg += msg

        if (len(full_msg) - HEADER_SIZE) == msg_len:
            # print("Full msg revieved.")
            # print(full_msg[HEADER_SIZE:])

            d = pickle.loads(full_msg[HEADER_SIZE:])
            print(d)

            new_msg = True
            full_msg = b''

    print(full_msg)