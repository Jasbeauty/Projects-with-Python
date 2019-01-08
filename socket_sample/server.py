#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2018/9/12 4:38 PM
# @Author: jasmine sun
# @File  : server.py


import socket

ip_port = ('127.0.0.1', 7070)
sk = socket.socket()
sk.bind(ip_port)
sk.listen(5)
while True:
    print("The server is starting .... ")
    conn, addr = sk.accept()
    print("The client address is ", str(addr))
    client_data = conn.recv(1024)
    print(client_data.decode('utf-8'))
    conn.send("server has responded ".encode('utf-8'))
    conn.close()
