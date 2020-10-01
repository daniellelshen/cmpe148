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
message = f.encode("utf-8")
try:
    clientSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    clientSocket.sendto(message,(serverName,serverPort))
except socket.error as err:
    print "error in socket creation: %s" %(err)
leapYears, serverAddress = clientSocket.recvfrom(2048)
leapYears = leapYears.decode("utf-8")
leapYears = leapYears.replace("u","")
print(leapYears)
clientSocket.close()