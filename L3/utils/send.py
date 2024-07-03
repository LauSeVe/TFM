#!/usr/bin/env python3

import os
from scapy.all import *

def main():
    pcap_file = "input.pcap"
    
    if pcap_file:
        packets = rdpcap(os.path.join(directory, pcap_file))
        sendp(packets, iface=interface)
    else:
        print("No file")

if __name__ == '__main__':
    directory = "." 
    interface = "enp7s0" 
    main()
