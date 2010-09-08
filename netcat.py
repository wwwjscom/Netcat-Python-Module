from socket import *

class Netcat:
    """Basic implementation of the nc unix command.  If alert,
    any connection issues will result in a thrown exception.  
    Otherwise, they will be handeled silently."""
    def __init__(self, hostname, port, alert = False):
        self.__createSocket()
        self.hostname = hostname
        self.port = port
        self.alert = alert
    def open(self):
        try:
            self.socket.connect((self.hostname, self.port))
        except error, msg:
            if self.alert:
                raise msg
    def close(self):
        try:
            self.socket.shutdown(SHUT_WR)
            self.socket.close()
        except error, msg:
            if self.alert:
                raise msg
    def sendall(self, content):
        self.socket.sendall(content)
    def reconnect(self):
        self.socket = None
        self.__createSocket()
        self.open()
    def __createSocket(self):
        self.socket = socket(AF_INET, SOCK_STREAM)
