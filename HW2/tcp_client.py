import socket
import sys
serverName = 'localhost'
serverPort = 12000
try:
    file = open("years.txt", 'r')
    f = file.read()
    file.close()
except IOError:
    print "Error: File does not exist."
try:
    clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))
except socket.error as err:
    print "error in socket creation: %s" %(err)
message = f.encode("utf-8")
clientSocket.send(message)
leapYears = clientSocket.recv(1024)
leapYears = leapYears.decode("utf-8")
leapYears = leapYears.replace("u","")
print(leapYears)
clientSocket.close()