#!/usr/bin/env python3

from scapy.all import *
from scapy.contrib.igmp import *
pkt = Ether(src=RandMAC())/IP(src="192.168.1.237")/IGMP(type=0x16, gaddr="233.1.2.3")
pkt[IGMP].igmpize()
interfaces = ["enp1s0.101", "enp1s0.102", "enp1s0.103"]
for i in interfaces:
    sendp(pkt, iface=i)
#sendp(pkt, iface="enp1s0.101")