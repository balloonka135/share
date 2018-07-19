import hashlib
import base64 
import time

def checkAuthToken(token,secretKey,exp):

     msg = base64.b64decode(token).decode('utf-8')
     print (msg)
     rand,cltime,oper_id,sign=msg.split('.')

     currentTime = int (time.time())

     print (" %s  / %f"% (cltime,currentTime))

     if currentTime - int(cltime) > int(exp):
        return False
     mySign = hashlib.sha1((rand+cltime+oper_id+secretKey).encode('utf-8')).hexdigest()

     if sign == mySign:
        return True
     return False
  