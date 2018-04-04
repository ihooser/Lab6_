'''
Created on Apr 2, 2018

@author: ihooser
'''
import sys
import socket
import os

if __name__ == '__main__':
    pass


#reading in all the imputs
serverIP = sys.argv[1]
serverPort = int(sys.argv[2])
time_delay = sys.argv[3]
execute_times = sys.argv[4]
command = sys.argv[5]
print "The server IP is:", serverIP
print "The server Port is:", serverPort
print "The execution time is: ",execute_times
print "The command that is being executed is: ", command 

#combining all the imformation into one sting to send
Message = execute_times + " " + time_delay + " " + command

inputFrom = raw_input('Are you sending data using TCP or UDP:')

#sending data using UDP
if inputFrom == "udp" or inputFrom == "UDP":
    clientSock_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    clientSock_udp.sendto(Message, (serverIP, serverPort))
    while True:
        print "WAITING!!!!!!!!!! for server"
        data, server = clientSock_udp.recvfrom(1024)
        print  data
        print "the client is now closed"
        clientSock_udp.close() 
        break
        
#sending data using TCP
if inputFrom == "tcp" or inputFrom == "TCP":
    #byte_reading =1024
    temp = 0
    #setting up the socket
    print "you will be sending a command using TCP"
    clientSock_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSock_tcp.connect((serverIP, serverPort))
    while temp == 0:
        clientSock_tcp.send(Message)
        print "the data that was sent was: "
        print Message
        data_back = clientSock_tcp.recv(1024)
        break
    print data_back
    print "the client is now closing"
    clientSock_tcp.close()

    
    
 
    
    
    
    
    