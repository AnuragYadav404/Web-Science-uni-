import socket
import json

HOST = "127.0.0.1" # loopback interface
PORT = 64999

def urlParser(url):
    result = {}

    result["Url"] = url

    if "://" in url:
        scheme, url = url.split("://")
        result["Scheme"]=scheme

    # now remove fragments
    if "#" in url:
        url, fragment = url.split("#")
        result["Fragment"] = fragment

    # now remove query string

    if "?" in url:
        url, query = url.split("?")
        result["Query"] = query

    # now extract path
    if "/" in url:
        url, path = url.split("/", maxsplit=1)
        result["Path"] = path 

    # now extract domain and socket
    if ":" in url:
        url, socket = url.split(":")
        result["Socket"] = socket
    
    result["Domain"] = url

    return result
    





with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print("Connected by ", addr)
        while True:
            json_data = conn.recv(1024)
            if not json_data:
                break
            clientUrl = json.loads(json_data.decode())
            print("Received URL: ", clientUrl)
            parsedUrl = urlParser(url=clientUrl)
            conn.sendall(json.dumps(parsedUrl).encode())