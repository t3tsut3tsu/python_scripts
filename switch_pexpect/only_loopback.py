#!/usr/bin/env python3

import pexpect

sw = "192.168.1.200"
usr = "admin"
passwrd = "admin"

telnet = pexpect.spawn(f"telnet {sw}") #соединение
telnet.sendline(usr)
telnet.expect('[Pp]assword')
telnet.sendline(passwrd)

telnet.expect('[>#]') #до режима enable
telnet.sendline('enable')
telnet.expect('[>#]')

telnet.sendline('show ip interface')
telnet.expect('#')
telnet.before
show_output = telnet.before.decode('utf-8')
#print(show_output)

iface = show_output.split('Valid')
for i in iface:
    if 'loopback' in i:
        print(i + 'Valid')

telnet.close()