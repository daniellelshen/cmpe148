# import socket module
from socket import *
import sys  # In order to terminate the program


# import from http://128.238.251.26:6789/HelloWorld.html
def main():
    serverPort = 9876
    serverSocket = socket(AF_INET, SOCK_STREAM)
    
    # Prepare a sever socket
    serverSocket.bind(('', serverPort))
    serverSocket.listen(1)

    print('The webserver is now on port: ', serverPort)
    while True:
        # Establish the connection
        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()
        print('... before Try ...')
        
        try:
            print('... inside Try ...')
            message = connectionSocket.recv(1024)
            print(message, '::', message.split()[0], ':', message.split()[1])
            filename = message.split()[1]
            print(filename, ' ::', filename[1:])
            f = open(filename[1:])
            outputdata = f.read()
            print('Outputdata: ', outputdata)

            connectionSocket.send('\nHTTP/1.1 200 OK\n\n')
            connectionSocket.send(outputdata)
            connectionSocket.close()
            serverSocket.close()
            sys.exit()  # Terminate the program after sending the corresponding data

        except IOError:
            pass

            print("404 Not Found")
            connectionSocket.send('\HTTP/1.1 404 Not Found\n\n')

        break


    pass
# Send response message for file not found
# Fill in start
# Fill in end
# Close client socket
# Fill in start
# Fill in end


if __name__ == '__main__':
    main()
