Lab6 Remote Command
code written by: Indiana Hooser


Client:
The client will be receiving arguments from the user. Then the user will decide wether to use TCP or UDP.
After the command has been sent the client will receive data stateing how ong it took the command to run.
-arguments
	Server_IP-adress Server-port_Number time_delay execute_times command
	(example and tested)
	10.1.225.29 5005 2 3 ls -l
-notes
	1) Anything inputted after the execute_times will be considered part of the command
	2) The client must be running under the same protocol
Server:
The server will receive a execution count, time delay and a command. These will be seperated out and then displayed.
The command will be run the execution cout times and have the time delay time between each ececution time. then total
execution time will be sent back to the client.
-arguments
	Server_port_number
	(example and tested)
	5005
	(note) this port number must be the same Server port number stated in the client.
-notes
	1) To change the protocal Server is running a ctrl -c must be used
	2) The protocal that is used will be a keyboard input
