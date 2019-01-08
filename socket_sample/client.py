#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2018/9/12 4:47 PM
# @Author: jasmine sun
# @File  : client.py


import socket
ip_port = ('127.0.0.1', 7070)
sk = socket.socket()
sk.connect(ip_port)
sk.send("hello, i am from client".encode('utf-8'))
server_reply = sk.recv(1024)
print(server_reply.decode('utf-8'))
sk.close()