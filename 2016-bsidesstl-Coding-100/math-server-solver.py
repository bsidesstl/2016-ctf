#!/usr/bin/python

import pexpect
import sys

################################
# A program to solve math-server coding   
# challenge for BSidesSTL. 
# Written by Doc Hak
#
# Note: this solver uses pexpect.  It would likely be easier to just
# create the sockets and deal with the data manually.  But by the time
# I realized that I was too deep and stuborn, so I finished it this way.
#
# Note 2: This one solves the problems a little differently than the
# actual math-server.py.  It imports operator, and uses it to solve
# the math problem.  Either way work, that way is probably a little more
# elegant, but this way is a little easier to understand.  
####################################

#User changable variables
target = '127.0.0.1'

#Global variables (Don't change!!)
counter = 1 #Used to count iterations
connected = 0 #test for connection
answer = 0.0000 #Used for storage of answer
problem = '' #Makes global variable

try: #Connect to server
	print "Connecting..."	
	id = pexpect.spawn('nc %s 9000'%target) #nc to target, change it above, aslo need nc
	#id.logfile = sys.stdout #Use this to debug, prints all sent and received to screen
	#id.logfile_read = sys.stdout #Sends all received data to screen
	id.expect_exact('=', 2) #Look for "=" in reply
	problem = id.before[59:] #The first math problem starts after the 59th character
	connected = 1 #Variable for noting we have connected to the server
except pexpect.ExceptionPexpect as e:
		print("Failed to connect to server.\nError: ")
		print(e)

if (connected):
	while (counter < 101): #If sucessfully connect, run it the requisit 100 times
		try: #solving, sending, receiving math
			problem = problem.split(' ') #Break the problem up by spaces for math below

			#Do math
			if problem[1] == '+':
				answer = float(problem[0]) + float(problem[2])
			if problem[1] == '-':
				answer = float(problem[0]) - float(problem[2])
			if problem[1] == '*':
				answer = float(problem[0]) * float(problem[2])
			if problem[1] == '/':
				answer = float(problem[0]) / float(problem[2])
			answer = float("{0:.2f}".format(answer)) #This formats it to two decimals

			#Send ansswer & get new problem
			if counter < 100: #If not time to grab the flag
				id.sendline('%s' %answer) #Send answer
				id.expect_exact(' =', 2) #Get result
				if 'Correct!' in id.before.split('\n')[1]: #Success 
# This takes the reply before the '=', which is a big string, splits it by newlines, 
# then compares the second line to see if it contains the string "Correct!".
					print 'Question #%d answered correctly! ' %counter #Just helps keep track
					counter += 1 #Count					
					problem = id.before.split('\n')[2]
				else: #Failed
					print 'Math failed!\n'
					id.close() #Close connection
					sys.exit() #Exit program because I fail....
			elif counter == 100:
				id.sendline('%s' %answer)
				id.expect_exact('}', 2)
				print 'Question #%d answered correctly! ' %counter #Just helps keep track
				print 'Flag: %s}' %id.before.split('\n')[2]
				id.close()
				sys.exit()
		except pexpect.EOF: #Catch end of file exception (Not expected)
			print 'EOF Flag: ', id.before.split('\n')[0:]
			id.close()
			sys.exit()
		except pexpect.ExceptionPexpect as e: #Catch unknown exceptions
			print("Mathing failed\nError: ")
			print(e)
else: id.close() #Close session


