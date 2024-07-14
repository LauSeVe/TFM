#!/usr/bin/env python3

import socket
import sys
from time import sleep

from scapy.all import *
from scapy.layers.inet import _IPOption_HDR


def get_if():
    ifs=get_if_list()
    iface=None # "h1-eth0"
    for i in get_if_list():
        if "enp7s0" in i:
            iface=i
            break;
    if not iface:
        print("Cannot find enp7s0 interface")
        exit(1)
    return iface

TYPE_EPHeader = 0x93

class EPHeader(Packet):
    Name = "EPHeader"
    fields_desc = [
        BitField("hawkID", 0, 16),
        BitField("exercise", 0, 4),
        BitField("ethernet", 0, 1),
        BitField("ipv4", 0, 1),
        BitField("ipv6", 0, 1),
        BitField("correct", 0, 1),
        StrFixedLenField("info", b"\x00" * 20, length=20),
    ]
bind_layers(IP, EPHeader, proto=TYPE_EPHeader)

class SwitchTrace(Packet):
    fields_desc = [ IntField("swid", 0),
                  IntField("qdepth", 0)]
    def extract_padding(self, p):
                return "", p

class IPOption_MRI(IPOption):
    name = "MRI"
    option = 31
    fields_desc = [ _IPOption_HDR,
                    FieldLenField("length", None, fmt="B",
                                  length_of="swtraces",
                                  adjust=lambda pkt,l:l*2+4),
                    ShortField("count", 0),
                    PacketListField("swtraces",
                                   [],
                                   SwitchTrace,
                                   count_from=lambda pkt:(pkt.count*1)) ]


def main():

    if len(sys.argv)<3:
        print('pass 2 arguments: <src> <dst> <n>')
        exit(1)
    rawValue = 0
    src = sys.argv[1]
    dst = sys.argv[2]
    iface="enp7s0"

    
    try:
      for i in range(int(sys.argv[3])):
        pkt = Ether(src=f"22:33:44:55:66:0{src}", dst=f"22:33:44:55:66:{src}1") / \
         IP(src=f"135.41.{src}.1", dst=f"135.41.{dst}.1", proto=147, options=IPOption_MRI(count=0, swtraces=[])) / \
         EPHeader(hawkID=4010, exercise=0, ethernet=0, ipv4=0, ipv6=0, correct=0, info='0') / \
         Raw(rawValue.to_bytes(4, byteorder='big'))
        sendp(pkt, iface=iface)
        rawValue = rawValue + 1
        sleep(1)
    except KeyboardInterrupt:
        raise


if __name__ == '__main__':
    main()