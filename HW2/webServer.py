# import socket module
from socket import *
import sys  # In order to terminate the program


# import from http://128.238.251.26:6789/HelloWorld.html
def main():
    serverPort = 6789
    serverHost = '127.0.0.1'
    serverSocket = socket(AF_INET, SOCK_STREAM)

    # Prepare a sever socket
    serverSocket.bind(('', serverPort))
    serverSocket.listen()

    print('The webserver is now on port: ', serverPort)
    while True:
        # Establish the connection
        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()
        print('... before Try ...')

        try:
            print('... inside Try ...')
            message = connectionSocket.recv(1024)
            #print(message, '::', message.split()[0], ':', message.split()[1])
            filename = message.split()[1]
            #print(filename, ' ::', filename[1:])
            f = open(filename[1:])
            outputdata = f.read()

            connectionSocket.send(bytes('HTTP/1.1 200 OK', 'UTF-8'))

            # Send the content of the requested file to the client
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())
            connectionSocket.send("\r\n".encode())

            connectionSocket.close()

        except IOError:
            connectionSocket.send(bytes('HTTP/1.1 404 Not Found', 'UTF-8'))
            print("404 Not Found")

            connectionSocket.close()

        serverSocket.close()
        sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
    main()