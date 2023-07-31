import socket, threading, time, os, sys
from psutil import process_iter
from signal import SIGTERM 


class TCPconnection:
    def __init__(self):
        print("Server hört auf: "+socket.gethostbyname(socket.gethostname()))
        
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind(("", 50000)) 
        self.s.listen(1)
        self.kill = False
        self.window = None


    def setobserver(self, observer):
        self.observer = observer
        
    def startlistening(self):
        x = threading.Thread(target=self.listener, args=(), daemon=True)
        x.start()
             
    def listener(self):
        try: 
            while True: 
                self.komm, self.addr = self.s.accept()
                while True: 
                    data = self.komm.recv(1024) 
                    if self.kill == True or data.decode() == "exitt":
                        break
                    if len(data.decode()) > 1:
                        print("[{}] {}".format(self.addr[0], data.decode()))
                        self.window.appendMessage(data.decode())
                        #self.observer.setmessage(data.decode())
        finally: 
            print("Server closed.")
            self.s.close()
            
    def sendmessage(self, message):
        self.komm.sendall(bytes(message,'utf-8'))
            
    @staticmethod
    def portcleaner():
        for proc in process_iter():
            for conns in proc.connections(kind='inet'):
                if conns.laddr.port == 50000:
                    proc.send_signal(SIGTERM) 
                    
    def getipaddr(self):
        return socket.gethostbyname(socket.gethostname())
    
    def setWindow(self, win):
        self.window = win

if __name__ == "main":
    y = TCPconnection()
    y.startlistening()



#TCPconnection.portcleaner()


# find port process
# netstat -ano | findstr :50000
# kill port process 
# taskkill /PID <PID> /F