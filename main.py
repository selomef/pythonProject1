# This is a sample Python script.

# import socket module
from socket import *
# In order to terminate the program
import sys


def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)
    # Prepare a server socket
    serverSocket.bind(("", port))
    # Fill in start
    serverSocket.listen(1)
    # Fill in end
    while True:
        # Establish the connection
        # print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()

        try:
                message =  connectionSocket.recv(1024)
                filename = message.split()[1]
                f = open(filename[1:])
                outputdata = f.read()
                # Send one HTTP header line into socket.
                connectionSocket.send(b'HTTP/1.0 200 OK\r\n\r\n')
                # Fill in start
                # Fill in end
                # Send the content of the requested file to the client
                for i in range(0, len(outputdata)):
                    connectionSocket.send(outputdata[i].encode())
                connectionSocket.send("\r\n".encode())
                connectionSocket.close()
        except IOError:
        # Send response message for file not found (404)
                  connectionSocket.send(b'404 file Not Found')
                  connectionSocket.close()
if __name__ == "__main__":
  webServer(13331)