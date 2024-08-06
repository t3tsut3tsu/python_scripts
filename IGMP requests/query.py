#!/usr/bin/env python3

from scapy.all import *
from scapy.contrib.igmp import *
pkt = Ether(src="e0:d9:e3:b4:00:06")/Dot1Q(vlan=100)/IP(src="192.168.1.230")/IGMP(type=0x11, gaddr="0.0.0.0")
pkt[IGMP].igmpize()
sendp(pkt, iface="enp1s0.104")
