#!/usr/bin/env python3

from scapy.all import *
from scapy.contrib.igmp import *
pkt = Ether(src="e0:d9:e3:b4:00:05", dst="01:00:5e:01:02:03")/Dot1Q(vlan=100)/IP(src="192.168.1.230", dst="233.1.2.3", ttl=64)/UDP(sport=5000, dport=5100)
sendp(pkt, iface='enp1s0.104', loop=True)
