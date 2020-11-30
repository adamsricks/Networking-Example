from mysocket import MySocket

def main():
    socket = MySocket()
    # connect to slicey boi
    socket.connect("192.168.1.21", 80)
    socket.mysend("message")
    socket.sock.close()

if __name__ == "__main__":
    main()