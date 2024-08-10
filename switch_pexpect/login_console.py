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

#telnet.close()