import requests
import socket
import json

def RosUpdate(aksi,ruangan): 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("192.168.43.49", 7777))
    sock.listen(5)

    jsonData = {"aksi":str(aksi),"ruangan":str(ruangan)}
    jsonData = json.dumps(jsonData)

    while True:
        (conn, addr) = sock.accept()
        conn.send(jsonData.encode("UTF-8"))

RosUpdate("antar", "satu kosong satu")