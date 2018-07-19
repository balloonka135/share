from tornado import websocket
from lib.Config import secretKey,expireSec
from lib.AuthToken import checkAuthToken

import base64 

class BaseWebSocket(websocket.WebSocketHandler):

    def check_origin(self, origin):
        #print ("origin",origin)
        return True

    def open(self,token):
        #print("received cookies: ", self.request.cookies)
        #print("received 'myuser': ", self.get_cookie("SESSIONID"))
        if not checkAuthToken(token,secretKey,expireSec):
           self.close()