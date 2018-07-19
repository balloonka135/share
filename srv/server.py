#!/usr/bin/python3

from tornado import websocket
import tornado.ioloop
import shlex, subprocess
import os
import sys
import time
import platform
import asyncio
import configparser

### import tools class (call ext. programs)

from lib.CmdWebSocket import CmdWebSocket

### imports my classes (dig ping etc) .... 
###
### [(r"/tools/(.*)", CmdWebSocket),(r"/api/(.*)", ApiWebSocket))]


app = tornado.web.Application([(r"/tools/(.*)", CmdWebSocket)])

if __name__ == "__main__":
    server = tornado.httpserver.HTTPServer(app)
    server.bind(1234)
    server.start(2)
    tornado.ioloop.IOLoop.instance().start()