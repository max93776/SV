from multiprocessing import Pipe, Process

class Sender:
    def __init__(self, conn):
        self.conn = conn

    def send_data(self, data):
        self.conn.send(data)

class Receiver:
    def __init__(self, conn):
        self.conn = conn

    def receive_data(self):
        data = self.conn.recv()
        return data

def run_sender(conn):
    sender = Sender(conn)
    sender.send_data("Hello from Sender!")

def run_receiver(conn):
    receiver = Receiver(conn)
    data = receiver.receive_data()
    print("Received data:", data)

if __name__ == "__main__":
    parent_conn, child_conn = Pipe()

    sender_process = Process(target=run_sender, args=(child_conn,))
    receiver_process = Process(target=run_receiver, args=(parent_conn,))

    sender_process.start()
    receiver_process.start()

    sender_process.join()
    receiver_process.join()
