from socket import *

import os

import sys

import struct

import time

import select

import binascii

ICMP_ECHO_REQUEST = 8


def checksum(str):
    csum = 0

    countTo = (len(str) / 2) * 2

    count = 0

    while count < countTo:
        thisVal = ord(str[count + 1]) * 256 + ord(str[count])

        csum = csum + thisVal

        csum = csum & 0xffffffff

        count = count + 2

    if countTo < len(str):
        csum = csum + ord(str[len(str) - 1])

        csum = csum & 0xffffffff

    csum = (csum >> 16) + (csum & 0xffff)

    csum = csum + (csum >> 16)

    answer = ~csum

    answer = answer & 0xffff

    answer = answer >> 8 | (answer << 8 & 0xff00)

    return answer


def receiveOnePing(mySocket, ID, timeout, destAddr):
    timeLeft = timeout

    while 1:

        startedSelect = time.time()

        whatReady = select.select([mySocket], [], [], timeLeft)

        howLongInSelect = (time.time() - startedSelect)

        if whatReady[0] == []:  # Timeout

            return "Request timed out."

        timeReceived = time.time()

        recPacket, addr = mySocket.recvfrom(1024)

        # Fill in start

        # Fetch the ICMP header from the IP packet

        # Fill in end



def sendOnePing(mySocket, destAddr, ID):
    # Header is type (8), code (8), checksum (16), id (16), sequence (16)

    myChecksum = 0

    # Make a dummy header with a 0 checksum.

    # struct -- Interpret strings as packed binary data



    # Calculate the checksum on the data and the dummy header.



    # Get the right checksum, and put in the header



        # Convert 16-bit integers from host to network byte order.

  # AF_INET address must be tuple, not str

    # Both LISTS and TUPLES consist of a number of objects

    # which can be referenced by their position number within the object


def doOnePing(destAddr, timeout):
    icmp = socket.getprotobyname("icmp")

    # SOCK_RAW is a powerful socket type. For more details see: http://sock-raw.org/papers/sock_raw

    # Fill in start

    # Create Socket here

    # Fill in end


    return delay


def ping(host, timeout=1):
    # timeout=1 means: If one second goes by without a reply from the server,

    # the client assumes that either the client’s ping or the server’s pong is lost


    # Send ping requests to a server separated by approximately one second



ping("www.poly.edu")


