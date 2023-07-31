<<<<<<< HEAD
import socket, threading, time

from psutil import process_iter
from signal import SIGTERM 

from multiprocessing import Pipe, Process 

class TCPconnection:
    def __init__(self):
        print("Server hört auf: "+socket.gethostbyname(socket.gethostname()))
        
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind(("", 50000)) 
        self.s.listen(1)
        self.kill = False
        
        x = threading.Thread(target=self.listener, args=(), daemon=True)
        x.start()
        print("Hier")
        time.sleep(10)
        self.kill = True

    
        
        
    def listener(self):
        try: 
            while True: 
                komm, addr = self.s.accept()
                while True: 
                    data = komm.recv(1024) 
                    if self.kill == True or data.decode() == "exit":
                        self.s.close()
                        break
                    print("[{}] {}".format(addr[0], data.decode())) 
                    nachricht = input("Antwort: ")
                    komm.send(nachricht.encode()) 
        finally: 
            self.s.close()
            
    @staticmethod
    def portcleaner():
        for proc in process_iter():
            for conns in proc.connections(kind='inet'):
                if conns.laddr.port == 50000:
                    proc.send_signal(SIGTERM) 

y = TCPconnection()
#TCPconnection.portcleaner()


# find port process
# netstat -ano | findstr :50000
# kill port process 
=======
import socket, threading, time

from psutil import process_iter
from signal import SIGTERM 

from multiprocessing import Pipe, Process 

class TCPconnection:
    def __init__(self):
        print("Server hört auf: "+socket.gethostbyname(socket.gethostname()))
        
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind(("", 50000)) 
        self.s.listen(1)
        self.kill = False
        
        x = threading.Thread(target=self.listener, args=(), daemon=True)
        x.start()
        print("Hier")
        time.sleep(10)
        self.kill = True

    
        
        
    def listener(self):
        try: 
            while True: 
                komm, addr = self.s.accept()
                while True: 
                    data = komm.recv(1024) 
                    if self.kill == True or data.decode() == "exit":
                        self.s.close()
                        break
                    print("[{}] {}".format(addr[0], data.decode())) 
                    nachricht = input("Antwort: ")
                    komm.send(nachricht.encode()) 
        finally: 
            self.s.close()
            
    @staticmethod
    def portcleaner():
        for proc in process_iter():
            for conns in proc.connections(kind='inet'):
                if conns.laddr.port == 50000:
                    proc.send_signal(SIGTERM) 

y = TCPconnection()
#TCPconnection.portcleaner()


# find port process
# netstat -ano | findstr :50000
# kill port process 
>>>>>>> bf6d9c38a44edca4613c01f8cd8294c0c185e8a3
# taskkill /PID <PID> /F