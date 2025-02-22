import socket
import json




HOST = "127.0.0.1" # loopback interface
PORT = 64999


url = "https://www.example.co.uk:443/blog/article/search?docid=720&hl=en#dayone"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))

    # here we get the url in destructured format
    client_socket.sendall(json.dumps(url).encode())
    json_data = client_socket.recv(1024)
    data = json.loads(json_data.decode())
    for key in data:
        print(key, " : ", data[key])



