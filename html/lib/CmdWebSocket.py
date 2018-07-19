from lib.BaseWebSocket import BaseWebSocket
import tornado.ioloop
import shlex, subprocess
import os
import sys
import time
import platform
import asyncio

class CmdWebSocket(BaseWebSocket):

    @tornado.web.asynchronous
    async def on_message(self, message):
        print ("newmsg")
        self.write_message(message)
        process = await asyncio.create_subprocess_exec ('ping', '-c','40', '8.8.8.8', stdout=asyncio.subprocess.PIPE )

        while True:
           line = await process.stdout.readline()
           if not line:
             break
           await self.write_message(line)
        self.write_message("done")

    def on_close(self):
        print ("Websocket closed")