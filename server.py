'''
Created on Apr 2, 2018

@author: ihooser
'''

def commit(execution_count,command,delay):
    start_time = time.time()
    print "start time: ", start_time
#     command = print "print this"
    for x in range (0,execution_count):
        os.system(command)
        time.sleep(float(delay))
        
           
    # end_time = int(datetime.datetime.now().strftime("%H%M%S"))
    end_time = time.time()
    print "end time: ", end_time
    execute_time = int(end_time-start_time)

    return execute_time

        
import os
import socket
import sys
#import datetime
import time
from time import gmtime, strftime
if __name__ == '__main__':
    pass

UDP_PORT_NO = int(sys.argv[1])
#getting the ip of the Server
UDP_IP_ADDRESS = socket.gethostbyname(socket.gethostname())
print "The server address is: ", UDP_IP_ADDRESS
print "The server port being used is: ", UDP_PORT_NO

inputFrom = raw_input('Are you reciving data using TCP or UDP:')

#sending data using UDP
if inputFrom == "udp" or inputFrom == "UDP": 
    serverSock_UDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serverSock_UDP.bind((UDP_IP_ADDRESS, UDP_PORT_NO))
    while True:
        print "_______________________________"
        print "WAITING for client_using UDP"
        data, addr = serverSock_UDP.recvfrom(1024)
        time_date = time.asctime(time.localtime(time.time()))
        splitter = data.split()
        command = splitter[2]
        print time_date, "adress: ", addr, "command: ", command , " 'connected'"
        execution_count = int(splitter[0])
        time_delay = int(splitter[1])
        execution_count = commit(execution_count,command,time_delay)
        send_Back = "The excecution took: " + str(execution_count)+ "sec"
        print send_Back
        if send_Back:
            serverSock_UDP.sendto(send_Back, addr)
            time_date = time.asctime(time.localtime(time.time()))
            print time.asctime(time.localtime(time.time())), " adress: ", addr, " disconnected"
    #     print " the data has been sent out"


if inputFrom == "TCP" or inputFrom == "tcp":
    serverSock_TCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSock_TCP.bind((UDP_IP_ADDRESS, UDP_PORT_NO))
    while True:
        serverSock_TCP.listen(1)
        print "_______________________________"
        print "WAITING for client_using TCP"
        connection, addr = serverSock_TCP.accept()
        data = ""
        while 1:
            data = connection.recv(1024)
            time_date = time.asctime(time.localtime(time.time()))
            spliter = data.split()
            command = spliter[2]
            # print command
            print time_date, "adress: ", addr, "command: ", command , "connected"
#             print "data at 0 is: ", spliter[0]
#             print "data at 1 is: ", spliter[1]
            execution_count = int(spliter[0])
            time_delay = float(int(spliter[1]))
            execution_count = commit(execution_count,command, time_delay)
            return_message = "The excecution took: " + str(execution_count)+ "sec"
            print return_message
            connection.send(return_message)
            print time.asctime(time.localtime(time.time())), " adress: ", addr, " disconnected"
            break

