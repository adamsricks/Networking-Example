from mysocket import MySocket

def main():
    socket = MySocket()
    # connect to oldo
    socket.connect("192.168.1.21", 80)
    socket.mysend("message")
    socket.sock.close()

if __name__ == "__main__":
    main()