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
        try:
            message = connectionSocket.recv(1024)
            print(message)
            filename = message.split()[1]
            print(filename)
            f = open(filename[1:])
            outputdata = f.read()
            print("output data: ", outputdata)
            # Send the HTTP response header line to the connection socket
            connectionSocket.send(bytes('HTTP/1.1 200 OK', 'UTF-8'))

            # Send the content of the requested file to the client
            print("Sending file to client\n")
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode('utf-8'))
            connectionSocket.send("\r\n".encode())
            print("... socket now closing ...\n")
            connectionSocket.close()

        except IOError:
            #send 404 ERROR to client
            connectionSocket.send(b"HTTP/1.1 404 Not Found\r\n\r\n")
            connectionSocket.send(b"<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n")
            print("404 Not Found")

            connectionSocket.close()

    serverSocket.close()
    sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
    main()