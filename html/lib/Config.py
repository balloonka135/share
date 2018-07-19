import configparser

config = configparser.ConfigParser()
config.read("server.conf")
secretKey = config.get("configuration","secretKey")
expireSec = config.get("configuration","expireSec")