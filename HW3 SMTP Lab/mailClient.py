from socket import *
import base64
import time
import ssl
from base64 import *
from getpass import getpass


def main():

    yourEmail = "daniellelshen@gmail.com"
    print("get password")

    yourPass = getpass("Enter your email password: ")
    print("got password")

    msg = "\r\n CMPE 148: I love computer networks!"
    endmsg = "\r\n.\r\n"
    # Choose a mail server (e.g. Google mail server) and call it mailserver
    mailserver = ("smtp.gmail.com", 587)  # Fill in start #Fill in end

    # Create socket called clientSocket and establish a TCP connection with mailserver
    # Fill in start
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect(mailserver)
    # Fill in end

    recv = clientSocket.recv(1024).decode()
    print(recv)
    if recv[:3] != '220':
        print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    print(recv1)
    if recv1[:3] != '250':
        print('250 reply not received from server.')

    # Sign into account to send email
    strtlscmd = "STARTTLS\r\n".encode()
    clientSocket.send(strtlscmd)
    recv2 = clientSocket.recv(1024)

    sslClientSocket = ssl.wrap_socket(clientSocket)

    emailAddress = b64encode(yourEmail.encode())
    emailPassword = b64encode(yourPass.encode())

    authorizationcmd = "AUTH LOGIN\r\n"

    sslClientSocket.send(authorizationcmd.encode())
    recv2 = sslClientSocket.recv(1024)
    print(recv2)

    sslClientSocket.send(emailAddress + "\r\n".encode())
    recv3 = sslClientSocket.recv(1024)
    print(recv3)

    sslClientSocket.send(emailPassword + "\r\n".encode())
    recv4 = sslClientSocket.recv(1024)
    print(recv4)

    # Send MAIL FROM command and print server response.
    # Fill in start
    mailFrom = "MAIL FROM: <{}>\r\n".format(yourEmail)
    clientSocket.send(mailFrom.encode())
    recv5 = sslClientSocket.recv(1024)
    print("After MAIL FROM command: " + recv5)
    if recv5[:3] != '250':
        print('250 reply not received from server.')
    # Fill in end

    # Send RCPT TO command and print server response.
    # Fill in start
    rcptTo = "RCPT TO:  <{}>\r\n".format(yourEmail)
    clientSocket.send(rcptTo.encode())
    recv6 = clientSocket.recv(1024).decode()
    print("After RCPT TO command: " + recv6)
    if recv6[:3] != '250':
        print('250 reply not received from server.')
    # Fill in end

    # Send DATA command and print server response.
    # Fill in start
    data = "DATA\r\n"
    sslClientSocket.send(data.encode())
    recv7 = sslClientSocket.recv(1024)
    print("After DATA command: " + recv7)
    if recv7[:3] != '250':
        print('250 reply not received from server.')
    # Fill in end

    # Send message data.
    # Fill in start
    subject = "Subject: CMPE 148 SMTP mail client testing \r\n\r\n"
    message = msg
    sslClientSocket.send("Subject: {}\n\n{}".format(subject, msg).encode())

    clientSocket.send(message.encode())
    clientSocket.send(endmsg.encode())
    recv_msg = clientSocket.recv(1024).decode()
    print("Response after sending message body:" + recv_msg)
    if recv_msg[:3] != '250':
        print('250 reply not received from server.')
    # Fill in end

    # Message ends with a single period.
    # Fill in start
    sslClientSocket.send(endmsg.encode())
    recv8 = sslClientSocket.recv(1024)
    print("Response after sending message body:" + recv8)
    if recv8[:3] != '250':
        print('250 reply not received from server.')
    # Fill in end

    # Send QUIT command and get server response.
    # Fill in start
    quitCmnd = 'QUIT\r\n'
    sslClientSocket.send(quitCmnd.encode())
    recv9 = sslClientSocket.recv(1024)
    print("Response after sending quit command:" + recv9)
    if recv9[:3] != '250':
        print('250 reply not received from server.')

    sslClientSocket.close()
    print('Was successful!')
    # Fill in end

# main code to run
if __name__ == "__main__":
    main()
