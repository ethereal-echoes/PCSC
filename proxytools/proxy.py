import socket, time
ssocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssocket.bind(('0.0.0.0', 8888))
ssocket.listen(1)
connection, _ = ssocket.accept()

def get_apdu_response(apdu_command):
    # implement your parser and response generator here
    apdu_response = []
    return apdu_response

while True:
    try:
        # we assumed each APDU command is at most 200 bytes
        apdu_command = csocket.recv(200)
        if len(apdu_command):
            print(f"APDU Command ===> {apdu_command.hex()}")
            apdu_response = get_apdu_response(apdu_command)
            response_len = len(apdu_response).to_bytes(1,"little")
            csocket.send(response_len)
            if response_len:
                csocket.send(resp)
                print(f"APDU Response <=== {apdu_response.hex()}")
            else:
                print(f"APDU Response <=== Real-Card-Response"
    except:
        print("Exception!")
        break

