import socketserver as sock
import time
import threading



class Service(sock.BaseRequestHandler):
    allow_reuse_address = True
    
    # Connection handler
    def handle(self):
        print("[+] Incoming connection")
        self.send("Question: Where is the University of New Haven?")
        if self.receive() == "West Haven": 
            self.send("[+] Bingo!")
        else: 
            self.send("[-] Try again!")
   

    # Function to send the challenge to clients
    def send(self, string, newline=True):
        if newline: string = string + "\n"
        self.request.sendall(string.encode())

    # Function to receive responses from clients
    def receive(self, prompt="\033[33m[?]\033[0m Print your answer here: "):
        self.send(prompt, newline=False)
        return self.request.recv(4096).strip().decode('ASCII')

class ThreadService(sock.ThreadingMixIn, sock.TCPServer, sock.DatagramRequestHandler):
    pass
    

def main():
    host = '0.0.0.0'
    port = 1337

    s = Service
    server = ThreadService((host, port), s)

    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()

    print ("[ Server started on port: ", str(port), "]")

    while(True): time.sleep(1)


if (__name__=="__main__"):
    main()