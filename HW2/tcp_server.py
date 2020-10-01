import socket
import sys
serverPort = 12000
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print "the server is ready to recieve"
while True:
    connectionSocket, addr = serverSocket.accept()
    year_cases = connectionSocket.recv(1024)
    year_cases = year_cases.decode("utf-8")
    years = []
    year_cases = year_cases.split()

    l = len(year_cases)
    for i in range(l):
        if(int(year_cases[i])%4==0 and int(year_cases[i])%100!=0 or int(year_cases[i])%400==0):
            info =(year_cases[i]+" is a leap year")
            years.append(info)
        else:
            info=(year_cases[i]+" is not a leap year")
            years.append(info)
    found_years = str(years).encode("utf-8")
    connectionSocket.send(found_years)
    connectionSocket.close()
