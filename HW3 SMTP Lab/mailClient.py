from getpass import getpass
from socket import *
import base64
import ssl
import time


def main():

    msg = "\r\n  CMPE 148 Lab 3: I love computer networks!"
    endmsg = "\r\n.\r\n"
    # Choose a mail server (e.g. Google mail server) and call it mailserver
    mailserver = ("smtp.gmail.com", 587)  # Fill in start #Fill in end

    # Create socket called clientSocket and establish a TCP connection with mailserver
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect(mailserver)


    recv = clientSocket.recv(1024)
    recv = recv.decode()
    print("Message after connection request:" + recv)
    if recv[:3] != '220':
        print('220 reply not received from server.')
    # Send HELO command and print server response.
    heloCommand = 'EHLO Microsoft\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024)
    recv1 = recv1.decode()
    print("Message after EHLO command:" + recv1)
    if recv1[:3] != '250':
        print('250 reply not received from server.')

    tls = "STARTTLS\r\n"
    clientSocket.send(tls.encode())
    recv = clientSocket.recv(1024)
    print("TLS: " + recv.decode())
    clientSocket = ssl.wrap_socket(clientSocket)

    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024)
    recv1 = recv1.decode()
    print("Message after EHLO command:" + recv1)

    # Info for username and password
    # Authortization
    username = input("Please enter your gmail: ")
    password = input("Please enter password: ")
    base64_str = ("\x00" + username + "\x00" + password).encode()
    base64_str = base64.b64encode(base64_str)
    base64_str = base64_str.strip("\n".encode())
    authMsg = "AUTH PLAIN ".encode() + base64_str + "\r\n".encode()
    clientSocket.send(authMsg)
    recv_auth = clientSocket.recv(1024)
    print("After auth: " + recv_auth.decode())

    # Send MAIL FROM command and print server response.
    mailFrom = "MAIL FROM: <{}>\r\n".format(username)
    clientSocket.send(mailFrom.encode())
    recv2 = clientSocket.recv(1024)
    recv2 = recv2.decode()
    print("After MAIL FROM command: " + recv2)

    # Send RCPT TO command and print server response.
    rcptTo = "RCPT TO: <{}>\r\n".format(username)
    clientSocket.send(rcptTo.encode())
    rcptTo = "RCPT TO: <{}>\r\n".format(username)
    clientSocket.send(rcptTo.encode())
    recv3 = clientSocket.recv(1024)
    recv3 = recv3.decode()
    print("After RCPT TO command: " + recv3)


    # Send DATA command and print server response.
    data = "DATA\r\n"
    clientSocket.send(data.encode())
    recv4 = clientSocket.recv(1024)
    recv4 = recv4.decode()
    print("After DATA command: " + recv4)
    # Fill in end

    # Send message data.
    subject = "Subject: CMPE148 SMTP Lab \r\n\r\n"
    clientSocket.send(subject.encode())
    date = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())
    date = date + "\r\n\r\n"
    clientSocket.send(date.encode())
    clientSocket.send(msg.encode())

    # Message ends with a single period.
    clientSocket.send(endmsg.encode())
    recv_msg = clientSocket.recv(1024)
    print("Response after sending message body:" + recv_msg.decode())

    # Send QUIT command and get server response.
    quit = "QUIT\r\n"
    clientSocket.send(quit.encode())
    recv5 = clientSocket.recv(1024)
    print(recv5.decode())
    clientSocket.close()

# main code to run
if __name__ == "__main__":
    main()
