'''
This is a coding challenge worth 100 points
for BSidesSTL 2016.
The user is told to create a program to connect to a server and solve
100 math problems flawlesly

Flag: {STL-<1luvzD4C0de>}

--Written from template by @Doc_Hak
--Template from http://www.binarytides.com/python-socket-server-code-example/
'''

import socket
import sys
import time
from thread import *
import operator
import random

HOST = ''   # Symbolic name meaning all available interfaces
PORT = 9000 # Non-privileged port

ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.div}

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'

#Bind socket to local host and port
try:
	s.bind((HOST, PORT))
except socket.error as msg:
	print 'Bind failed. Error Code : %s Message %s' %(str(msg[0]),msg[1])
	sys.exit()
print 'Socket bind complete'
 
#Start listening on socket
s.listen(10)
print 'Socket now listening'

#Function for handling connections. This will be used to create threads
def clientthread(conn):
	try:
		#Define some messages & variables
		greetings = 'Welcome to BSidesCTF %s.\nI heard you like math...\n' %addr[0]
		correctAnswer = 'Correct!\n'
		incorrectAnswer = 'Try harder...\n Hint: two decimal places where applicable (1.01 + .09 = 1.1)\n'
		flag = '{STL-<1luvzD4C0de>}'
		counter = 0
		operatorList = ['+','-','*','/']

		#send message to connected client
		conn.send('%s' %greetings) #greetz

		#infinite loop so that function does not terminate and thread does not end.
		while counter < 100:
			for i in range(100): #100 math problems
				#Creat Math Problem
				fnum = float("{0:.2f}".format(random.uniform(1, 100))) #random float between 1 & 100, 2 decimal places
				snum = float("{0:.2f}".format(random.uniform(1, 100)))
				operator = operatorList[random.randint(0,3)] #choose a random operator from the list
				#Solve Math Problem
				op_func = ops[operator] #This does a lookup of the operator in the global dictionary
				answer = float("{0:.2f}".format(op_func(fnum, snum))) #uses the operator on the numbers (ex: 2.01 * 3.68), limits answer to 2 decimal places
				answer = str(answer) #sets answer as string for comparison to received data
				#Send Math Problem
				conn.sendall('%s %s %s = ' %(fnum, operator, snum)) #Send the problem
				#Receive and check for answer
				data = conn.recv(1024) #Receive user answer
				if data.strip('\n') == answer: #strips new line, compares to correct answer, if correct:
					#Correct
					conn.sendall('%s' %correctAnswer)
					counter += 1
				elif data.strip('\n') != answer: 
					#Incorrect
					conn.sendall('%s' %incorrectAnswer)
					conn.close() #kicks user
					break
				elif not data: #Umm, no data received, go ahead and count it incorrect
					conn.sendall('%s' %incorrectAnswer)
					conn.close()
					break
		if counter == 100: #user has correctly answered 100 problems
			print 'Sent flag to %s\n' %addr[0] #alert CTF staff flag was sent
			conn.sendall('%s\n' %flag) #Send flag
			conn.close() #kbai
	except socket.error as e: #User rage quit lol
		#print 'Socket error: ', e	
		conn.close()
	except Exception as e: #Other exception not expected
		print 'Exception: ', e
		conn.close()
	except KeyboardInterrupt: #CTF staff hit ctl + c
		conn.close() #Kick connections
		sys.exit() #gracefully close
	finally:	#If all else fails, drop connection
		#came out of loop
		conn.close() #kbai

#Program logic to set up and accept connections, call math problem
try:
	while 1: #fooorreeeevveeeerrrrr
		#wait to accept a connection - blocking call
		conn, addr = s.accept()
		print 'Connected with %s:%s' %(addr[0], str(addr[1]))

		#start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
		start_new_thread(clientthread ,(conn,))
except KeyboardInterrupt: #CTF staff hit ctl + c
	conn.close() #Drop connection
	s.close() #Close socket
	sys.exit() #die
finally: #All else fails
	s.close() #This makes sure program doesn't keep blocking port after ctrl+c.  
#Note, if ctrl+c is given with a client connected it'll still block the port for ~10 seconds.
	sys.exit() #die

